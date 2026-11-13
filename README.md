# OmniHealth AI — Voice & Chat Patient Concierge

OmniHealth AI is an autonomous 24/7 patient concierge and intake assistant engineered for international healthcare and medical tourism networks (modeled after the **PlacidWay** global coordination standard). It consults prospective international patients on procedure packages, upfront price estimates, surgeon credentials, travel logistics, and captures consultation bookings directly into a real-time CRM coordination pipeline across accredited hospital partner clinics in Bangkok and Istanbul.

🌐 **Live Production Portal:** [https://omnihealth-ai-id.vercel.app](https://omnihealth-ai-id.vercel.app)  
📊 **Live Patient Intake CRM:** [Google Sheets 24/7 Cloud Pipeline](https://docs.google.com/spreadsheets/d/1Oq_fT7H_2zF8q7l9-X6Wp9vA5j9U2b/edit)  
📁 **Repository:** [https://github.com/yusufarifin100/omnihealth-ai](https://github.com/yusufarifin100/omnihealth-ai)

---

## 🎯 Purpose & Business Impact
International medical tourism requires prompt qualification: patients considering dental smile makeovers, LASIK, or executive health screenings in foreign destinations often drop out due to 48–72 hour email response delays. OmniHealth AI provides:
* **Instant 24/7 Multi-Channel Intake:** Voice (Speech-to-Text & Neural TTS) and interactive Chat widgets on web.
* **Grounded Clinical Knowledge (Zero Hallucination):** Pre-programmed medical packages ($4,200-$4,800 Dental Veneers, $1,650 LASIK, $450 Executive Health Checkup).
* **Automated Lead Capture:** Automatically captures patient name, email, phone/WhatsApp, chosen procedure, destination, and preferred appointment dates into CRM workflows for human medical coordinators.

---

## 🛠️ Architecture & Core Components

```
┌─────────────────────────────────┐
│  Patient (Web Browser / Voice)  │
└────────────────┬────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│  OmniHealth Web Portal (Vercel Edge CDN)               │
│  - Semantic HTML5, CSS3 Glassmorphism UI               │
│  - Voiceflow Web SDK & Live Speech Synthesizer         │
└────────────────┬───────────────────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│  OmniHealth Brain (Voiceflow Flash 4.2 / GPT-4o-mini)   │
│  - System Persona: Maya (Empathetic Medical Concierge) │
│  - Knowledge Base RAG: Bangkok & Istanbul Clinics       │
│  - Clinical Triage: Emergency Disclaimers              │
│  - Tool Calling: submit_booking_to_sheets              │
└────────────────┬───────────────────────────────────────┘
                 │
                 ▼ (Real-time HTTP POST Webhook)
┌────────────────────────────────────────────────────────┐
│  Automation & CRM Layer (Google Apps Script / n8n)     │
│  - 24/7 Serverless Webhook Endpoint                    │
│  - Real-Time Row Ingestion into Google Sheets CRM      │
│  - Automated Coordinator Alert / Email Dispatch        │
└────────────────────────────────────────────────────────┘
```

---

## 💻 Tech Stack
* **Conversational AI / Voice Engine:** Voiceflow (Agentic Architecture, Tool Calling, Deepgram STT, ElevenLabs TTS)
* **LLM Engine:** Voiceflow Flash 4.2 / OpenAI GPT-4o-mini
* **Frontend:** Vanilla HTML5, CSS3 (Modern Glassmorphic Healthcare Design), Vanilla JS
* **Cloud Hosting:** Vercel (Auto-deploy on Git push)
* **Automation & CRM Integration:** Google Apps Script Serverless Webhooks, Google Sheets CRM, n8n / Make.com Webhook Specification
* **API & Backend Specifications:** FastAPI (`webhooks/server.py`), JSON Schemas (`webhooks/sample_payload.json`)

---

## 📂 Project Structure

```
omnihealth/
├── index.html                  # Production landing page with Voiceflow Voice & Chat Widget
├── vercel.json                 # Vercel deployment and routing configuration
├── README.md                   # Complete architectural and operational documentation
├── docs/
│   ├── SYSTEM_PROMPT.md        # Maya agent prompt, conversational rules, triage boundary
│   ├── CLINIC_KNOWLEDGE_BASE.md# Grounded knowledge: treatments, pricing, doctor profiles
│   ├── CONVERSATION_FLOW.md    # Multi-turn patient intake & qualification flowcharts
│   └── SETUP_GUIDE.md          # Step-by-step setup guide for Voiceflow & webhook integrations
└── webhooks/
    ├── server.py               # Standalone FastAPI webhook receiver (Python backend)
    └── sample_payload.json     # Standardized JSON lead payload format
```

---

## 🚀 Live Demonstration Walkthrough

1. Visit **[https://omnihealth-ai-id.vercel.app](https://omnihealth-ai-id.vercel.app)**.
2. Click the **Chat / Microphone button** in the bottom-right corner.
3. Inquire about procedures:
   - *"Berapa biaya veneer gigi di Bangkok dan dokter siapa yang menangani?"*
   - *"What does the Executive Health Checkup in Istanbul include?"*
4. Confirm a consultation:
   - Provide your Name, Phone/WhatsApp, Email, and Target Date.
   - Maya triggers `submit_booking_to_sheets` and immediately confirms receipt.
5. The lead appears instantly in the medical coordinator's **Google Sheets CRM**.

---

## 🛡️ Clinical Disclaimer
*OmniHealth AI (Maya) is a patient intake concierge and medical tourism coordination assistant. Maya does not diagnose medical conditions, provide formal clinical prescriptions, or handle medical emergencies. For life-threatening emergencies, patients are instructed to immediately dial local emergency numbers (e.g., 911, 112, 1669, 119).*

---
*Created by [Ahmad Yusuf Arifin](https://github.com/yusufarifin100) for PlacidWay AI Medical Tourism Intake Assistant.*
