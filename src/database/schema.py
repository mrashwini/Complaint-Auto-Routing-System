from pydantic import BaseModel

class Complaint(BaseModel):
    complaint_id: str
    text: str
    category: str
    priority: str
    eta_days: int
    officer_id: str

class Officer(BaseModel):
    officer_id: str
    name: str
    department: str
    specialization: str
    language: str
    workload: int