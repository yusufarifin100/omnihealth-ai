# OmniHealth AI - Voice & Chat Patient Concierge

Simulation project for an international medical tourism concierge (PlacidWay standard).

## 📁 Project Structure

```
omnihealth/
├── docs/
│   ├── SYSTEM_PROMPT.md          # Production prompt for Voiceflow / Vapi / OpenAI
│   ├── CONVERSATION_FLOW.md       # Dialogue scenarios, handling objections, booking flow
│   └── CLINIC_KNOWLEDGE_BASE.md  # Medical procedures, packages, pricing, doctors & FAQ
├── webhooks/                     # Webhook handlers (n8n / FastAPI / Express)
│   └── sample_payload.json       # JSON output format sent to CRM / Google Sheets
└── README.md
```

## 🎯 Target Capabilities
- **Chat & Voice Ingestion**: Natural voice/chat assistant answering procedure questions, estimated costs, and doctor availability.
- **Medical Triage & Disclaimer**: Clear disclaimers that AI does not replace direct physician diagnosis.
- **Lead Capture & Booking**: Collects patient name, country/phone, preferred date, treatment interest, and symptoms/notes.
- **Automation Pipeline**: Trigger webhook to CRM/n8n/Google Sheets upon booking confirmation.
