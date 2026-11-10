"""
OmniHealth Webhook Receiver
Receives lead/booking payloads from Voiceflow / Vapi / Retell / n8n
and simulates forwarding to CRM or Google Sheets.
"""

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import json

app = FastAPI(title="OmniHealth Patient Webhook API", version="1.0.0")

class PatientData(BaseModel):
    patient_name: str
    phone: str
    email: Optional[str] = None
    treatment: str
    preferred_date: str
    notes: Optional[str] = ""

class ConsultationPayload(BaseModel):
    event: str = "patient_consultation_booked"
    timestamp: Optional[str] = None
    source: str = "Voiceflow_or_Vapi"
    channel: str = "voice_call"
    patient_data: PatientData
    crm_status: Optional[str] = "NEW_INQUIRY"

@app.get("/")
def health_check():
    return {"status": "ok", "service": "OmniHealth Webhook Receiver"}

@app.post("/webhook/booking")
async def receive_patient_booking(payload: ConsultationPayload):
    # Log incoming booking
    print(f"\n[🔔 NEW PATIENT BOOKING RECEIVED]")
    print(f"Name     : {payload.patient_data.patient_name}")
    print(f"Phone    : {payload.patient_data.phone}")
    print(f"Email    : {payload.patient_data.email}")
    print(f"Treatment: {payload.patient_data.treatment}")
    print(f"Date     : {payload.patient_data.preferred_date}")
    print(f"Notes    : {payload.patient_data.notes}")
    print(f"Channel  : {payload.channel}")
    
    # In production, forward to Google Sheets API, HubSpot, or n8n workflow
    return {
        "success": True,
        "message": f"Consultation for {payload.patient_data.patient_name} successfully recorded.",
        "booking_id": f"OMNI-{int(datetime.now().timestamp())}",
        "status": "FORWARDED_TO_PATIENT_COORDINATOR"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
