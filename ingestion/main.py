from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from ingestion.normalizer import normalize_alert
 branch/merin

app = FastAPI()

from ingestion.logger import logger
from ingestion.threat_lookup import check_ip_reputation
from ingestion.merge_alert import merge_alert

app = FastAPI(
    title="SOAR Incident Containment Engine",
    version="1.0"
)
 main

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

 branch/merin
    return {

        "status":"received",

        "normalized_alert":normalized,

        "message":"Alert normalized successfully"

    logger.info(
        f"Alert received ID={alert.id} IP={alert.src_ip}"
    )

    enrichment = check_ip_reputation(
        normalized.get("source_ip")
    )

    merged_alert = merge_alert(normalized, enrichment)

    logger.info(
        f"Threat lookup completed for {normalized.get('source_ip')}"
    )

    return {
        "status":"received",
        "alert": merged_alert,
        "message":"Alert received and enriched successfully"
 main
    }
