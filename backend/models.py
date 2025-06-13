from pydantic import BaseModel

class ComplaintRequest(BaseModel):
    name: str
    mobile: str
    complaint: str

class ComplaintResponse(BaseModel):
    message: str
    complaint_id: str

class StatusResponse(BaseModel):
    complaint_id: str
    status: str
