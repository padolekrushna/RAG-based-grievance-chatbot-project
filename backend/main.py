from fastapi import FastAPI, HTTPException
from models import ComplaintRequest, ComplaintResponse, StatusResponse
from database import create_table
from crud import register_complaint, get_complaint_status

app = FastAPI(title="Grievance Chatbot API")

# Initialize DB on startup
create_table()

@app.post("/register", response_model=ComplaintResponse)
def register_complaint_api(data: ComplaintRequest):
    complaint_id = register_complaint(data.name, data.mobile, data.complaint)
    return {"message": "Complaint registered successfully", "complaint_id": complaint_id}

@app.get("/status", response_model=StatusResponse)
def fetch_status(mobile: str):
    result = get_complaint_status(mobile)
    if not result:
        raise HTTPException(status_code=404, detail="Complaint not found.")
    return result
