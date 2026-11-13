# OmniHealth AI — Voice & Chat Patient Concierge

OmniHealth AI is a 24/7 autonomous patient concierge and intake assistant. It helps prospective patients inquire about medical packages, upfront pricing, and doctor availability in Bangkok and Istanbul, while capturing consultation bookings directly into Google Sheets in real time.

🌐 **Live Website:** [https://omnihealth-ai-id.vercel.app](https://omnihealth-ai-id.vercel.app)

---

## 🔄 System Flowchart

```mermaid
flowchart LR
    User([User / Patient]) -->|Chat / Voice Inquiry & Booking| Maya[Maya - Voiceflow AI Agent]
    Maya -->|Triggers Webhook: submit_booking_to_sheets| Script[Google Apps Script]
    Script -->|Append Row Real-Time| Sheets[(Google Sheets CRM)]
```

---

## 💻 Tech Stack
* **Conversational AI Platform:** Voiceflow (Agentic Architecture & Tool Calling)
* **LLM Engine:** Voiceflow Flash 4.2
* **Voice & Speech:** Deepgram (Speech-to-Text) & ElevenLabs (Voice Synthesis)
* **Frontend:** Vanilla HTML5, CSS3, Vanilla JS
* **Cloud Hosting:** Vercel
* **Automation & CRM Integration:** Google Apps Script, Google Sheets
* **API & Backend Specifications:** FastAPI (`webhooks/server.py`), JSON Schemas (`webhooks/sample_payload.json`)
