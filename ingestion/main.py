from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from ingestion.normalizer import normalize_alert
from ingestion.threat_lookup import check_ip_reputation
from ingestion.merge_alert import merge_alert
from ingestion.logger import (
    log_alert_received,
    log_enrichment_started,
    log_enrichment_completed,
    log_enrichment_failed
)

app = FastAPI(
    title="SOAR Incident Containment Engine",
    version="1.0"
)


class SIEMAlert(BaseModel):
    id: str
    time: datetime
    src_ip: str
    type: str
    host: str
    severity: str


@app.get("/")
def home():
    return {
        "message": "SOAR Incident Containment Engine is running"
    }


@app.post("/alerts")
def receive_alert(alert: SIEMAlert):

    # Convert Pydantic model to dictionary
    alert_data = alert.model_dump()

    # Normalize incoming alert
    normalized_alert = normalize_alert(alert_data)

    # Log alert reception
    log_alert_received(
        normalized_alert["alert_id"],
        normalized_alert["source_ip"]
    )

    # Start enrichment
    log_enrichment_started(
        normalized_alert["source_ip"]
    )

    try:

        enrichment = check_ip_reputation(
            normalized_alert["source_ip"]
        )


        log_enrichment_completed(
            normalized_alert["source_ip"],
            enrichment["reputation_score"]
        )

    except Exception as e:

        log_enrichment_failed(
            normalized_alert["source_ip"],
            str(e)
        )

        enrichment = {
            "ip": normalized_alert["source_ip"],
            "reputation_score": 0,
            "source": "lookup_failed",
            "country": "Unknown",
            "isp": "Unknown",
            "asn": "Unknown"
        }

    enriched_alert = merge_alert(
        normalized_alert,
        enrichment
    )
    
    return {

        "status": "received",

        "enriched_alert": enriched_alert,

        "message": "Alert received and enriched successfully"
    }
