from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from ingestion.normalizer import normalize_alert

app=FastAPI()

class SIEMAlert(BaseModel):
    id:str
    time:datetime
    src_ip:str
    type:str
    host:str
    severity:str

@app.post("/alerts")

def receive_alert(alert:SIEMAlert):

    normalized=normalize_alert(alert.model_dump())

    return {

        "status":"received",

        "normalized_alert":normalized,

        "message":"Alert normalized successfully"
    }
