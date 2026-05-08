from fastapi import FastAPI
from pydantic import BaseModel

from inference_pipeline import run_pipeline

app = FastAPI()

class ComplaintRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Complaint Auto Routing API"
    }

@app.post("/predict")
def predict(request: ComplaintRequest):
    result = run_pipeline(request.text)

    return result