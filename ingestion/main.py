from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from ingestion.normalizer import normalize_alert
from ingestion.logger import logger

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

    normalized=normalize_alert(alert.model_dump())

    logger.info(
        f"Alert received ID={alert.id} IP={alert.src_ip}"
    )
    
    return {

        "status":"received",

        "normalized_alert":normalized,

        "message":"Alert normalized successfully"
    }
