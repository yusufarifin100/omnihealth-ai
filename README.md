# OmniHealth AI - Voice & Chat Patient Concierge

Simulation project for an international medical tourism concierge (PlacidWay standard).

🌐 **Live Demo Website:** [https://yusufarifin100.github.io/omnihealth-ai/](https://yusufarifin100.github.io/omnihealth-ai/)

---

## 📁 Project Structure

```
omnihealth/
├── index.html                    # Production Landing Page with live Voiceflow widget
├── docs/
│   ├── SYSTEM_PROMPT.md          # Production prompt for Voiceflow / Vapi / OpenAI
│   ├── CONVERSATION_FLOW.md       # Dialogue scenarios, handling objections, booking flow
│   ├── CLINIC_KNOWLEDGE_BASE.md  # Medical procedures, packages, pricing, doctors & FAQ
│   └── SETUP_GUIDE.md            # Step-by-step Voiceflow & Vapi deployment guide
├── webhooks/                     # Webhook handlers (n8n / FastAPI / Express)
│   ├── sample_payload.json       # JSON output format sent to CRM / Google Sheets
│   └── server.py                 # FastAPI webhook receiver endpoint
└── README.md
```

## 🎯 Target Capabilities
- **Chat & Voice Ingestion**: Natural voice/chat assistant answering procedure questions, estimated costs, and doctor availability.
- **Medical Triage & Disclaimer**: Clear disclaimers that AI does not replace direct physician diagnosis.
- **Lead Capture & Booking**: Collects patient name, country/phone, preferred date, treatment interest, and symptoms/notes.
- **Automation Pipeline**: Trigger webhook to CRM/n8n/Google Sheets upon booking confirmation.

---
*Environment: Configured for local development on Home PC.*

## 🚀 How to Enable GitHub Pages:
1. Go to your repo **Settings** on GitHub -> **Pages**.
2. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
3. Select branch: `main` and folder: `/ (root)`, then click **Save**.
4. Your website will be live at `https://yusufarifin100.github.io/omnihealth-ai/`.
