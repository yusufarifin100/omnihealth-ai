# Conversation Flow & Scenarios

## 1. High-Level Flowchart

```mermaid
flowchart TD
    Start([Patient starts Chat or Voice Call]) --> Greet[Greeting & Intent Discovery]
    Greet --> Inquiry{Patient Question Type}
    
    Inquiry -->|Procedure & Pricing| PriceInfo[Explain Package, Pricing, Recovery & Inclusions]
    Inquiry -->|Doctor & Scheduling| DocInfo[Explain Specialist Credentials & Available Days]
    Inquiry -->|General Medical Tourism| TourismInfo[Explain Travel, Hotel, Airport Transfer]

    PriceInfo --> BookingPitch[Offer Free Telehealth or Clinic Consultation]
    DocInfo --> BookingPitch
    TourismInfo --> BookingPitch

    BookingPitch --> Intake{Patient Wants to Book?}
    Intake -->|Yes| CollectData[Collect: Full Name, WhatsApp/Phone, Email, Preferred Date, Notes]
    Intake -->|Hesitant / Not yet| SoftClose[Offer to send brochure via WhatsApp/Email]
    
    CollectData --> Confirmation[Read back confirmation & inform coordinator will reach out]
    Confirmation --> WebhookTrigger[Trigger Webhook -> CRM / Google Sheets / n8n]
    SoftClose --> WebhookTrigger
```

---

## 2. Conversation Steps & Scripts

### Phase 1: Welcoming & Triage
- **Voice Agent Opening:**
  > "Hello! Thank you for calling OmniHealth International Concierge. My name is Maya, your AI patient assistant. How may I assist you with your medical journey or appointments today?"
- **Chat Opening:**
  > "Welcome to OmniHealth Concierge! 🌟 I can help you with procedure costs, specialist schedules, and booking your initial consultation. What treatment or inquiry can I assist you with today?"

### Phase 2: Treatment Information & Pricing Breakdown
- **Patient:** "How much does a full set of dental veneers cost?"
- **Maya (AI):**
  > "Our full set of 16 E-Max porcelain veneers in our accredited clinic starts at $4,200 to $4,800. This includes your 3D digital smile scan, local hotel discounts, and airport VIP pickup. Treatment usually takes 5 to 7 days. Are you looking to travel soon, or would you like to speak with Dr. Aris Thorne for a virtual smile assessment first?"

### Phase 3: Intake / Lead Qualification (Required Fields)
Before confirming the appointment, the assistant must gather:
1. `full_name`: First and Last name.
2. `contact_number`: Phone number with country code (WhatsApp preferred).
3. `email`: Contact email address.
4. `treatment_interest`: Dental, LASIK, Health Checkup, or Other.
5. `preferred_date`: Desired date or timeframe (e.g., "Next month", "15 November").
6. `patient_notes`: Any pre-existing conditions, allergies, or questions.

### Phase 4: Confirmation & Hand-off
- **Maya (AI):**
  > "Thank you, [Name]! I've reserved a tentative consultation slot for [Date] with [Doctor/Department]. Our international patient coordinator will message you on WhatsApp at [Phone Number] within 2 business hours with your itinerary details and confirmation. Is there anything else I can prepare for you today?"

---

## 3. Edge Cases & Safety Protocols
- **Emergency Case:**
  - *Trigger:* Patient mentions chest pain, stroke symptoms, acute bleeding, or suicide.
  - *Bot Reaction:* Immediately state emergency disclaimer and urge calling local emergency services (911/112). Do not attempt to diagnose or schedule regular clinic appointments.
- **Ambiguous Request:**
  - *Trigger:* "I want surgery."
  - *Bot Reaction:* Clarify politely: "We specialize in dental transformations, laser eye surgery, and executive health screenings. Which area are you looking for?"
