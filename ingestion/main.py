from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class SIEMAlert(BaseModel):
    id: str
    time: datetime
    src_ip: str
    type: str
    host: str
    severity: str

@app.get("/")
def home():
    return {"message":"SOAR ingestion service is running"}

@app.post("/alerts")
def receive_alert(alert: SIEMAlert):

    return {
        "status":"received",
        "alert_id":alert.id,
        "source_ip":alert.src_ip,
        "message":"Alert received successfully"
    }
