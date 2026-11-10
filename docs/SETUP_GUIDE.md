# Quickstart Setup Guide: Voiceflow & Vapi.ai

Follow this guide to get your live demo ready for PlacidWay in under an hour.

---

## Option 1: Voiceflow Setup (Best for visual chat & voice widget)

1. **Create Project**:
   - Sign up at [Voiceflow.com](https://voiceflow.com) (Free Tier).
   - Create a new project: select **Web Chat** or **Voice Agent**.
2. **Upload Knowledge Base**:
   - Go to the **Knowledge Base** tab on the left menu.
   - Click **Add Data Source** -> Select Document/Text.
   - Copy-paste or upload [`docs/CLINIC_KNOWLEDGE_BASE.md`](file:///d:/SELF%20PROJECT/AppDev/omnihealth/docs/CLINIC_KNOWLEDGE_BASE.md).
3. **Configure System Prompt**:
   - In Settings / AI Model, paste the prompt from [`docs/SYSTEM_PROMPT.md`](file:///d:/SELF%20PROJECT/AppDev/omnihealth/docs/SYSTEM_PROMPT.md).
   - Choose Model: **GPT-4o-mini** (fast and cost-efficient) or **Claude 3.5 Sonnet**.
4. **Setup Webhook API Step**:
   - In Voiceflow canvas, add an **API Block** after patient details are collected.
   - Method: `POST`
   - URL: Your n8n webhook URL or ngrok endpoint pointing to `webhooks/server.py`.
   - Body: Raw JSON matching [`webhooks/sample_payload.json`](file:///d:/SELF%20PROJECT/AppDev/omnihealth/webhooks/sample_payload.json).
5. **Publish & Share**:
   - Click **Publish** -> **Share Prototype**.
   - Copy the public prototype link. This is the link you will send to PlacidWay!

---

## Option 2: Vapi.ai Setup (Industry Standard for Voice Phone Calls)

1. **Create Assistant**:
   - Go to [Vapi.ai](https://vapi.ai) dashboard -> **Assistants** -> **Create Assistant**.
   - Name: `OmniHealth Maya Concierge`.
2. **Configure Voice & Model**:
   - **Transcriber:** Deepgram (Nova-2, English or Multilingual).
   - **Model:** OpenAI `gpt-4o-mini`, Temperature: `0.3`.
   - **Voice:** Cartesia or ElevenLabs (e.g., *Jessica* or *Sarah* - calm, warm healthcare tone).
   - **System Prompt:** Paste [`docs/SYSTEM_PROMPT.md`](file:///d:/SELF%20PROJECT/AppDev/omnihealth/docs/SYSTEM_PROMPT.md).
3. **Add Function/Tool (`book_consultation`)**:
   - In Vapi Tools tab, add a function `book_consultation`.
   - Define parameters: `patient_name`, `phone`, `email`, `treatment`, `preferred_date`, `notes`.
   - Server URL: Your webhook endpoint.
4. **Test & Share In-Browser Web Call**:
   - Click the test button in Vapi, or grab the Web Call widget code to embed on any webpage.
