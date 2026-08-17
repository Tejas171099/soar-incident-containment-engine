from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from ingestion.logger import setup_logger
from ingestion.normalizer import normalize_alert
from ingestion.threat_lookup import check_ip_reputation
from ingestion.merge_alert import merge_alert


app = FastAPI(
    title="SOAR Incident Containment Engine",
    description="Alert ingestion and threat intelligence enrichment API",
    version="1.0.0",
)

logger = setup_logger()


class SIEMAlert(BaseModel):
    id: str
    time: datetime
    src_ip: str
    type: str
    host: str
    severity: str


@app.get("/")
def root():
    """
    Health check endpoint.
    """
    return {
        "status": "running",
        "service": "SOAR Incident Containment Engine",
    }


@app.post("/alerts")
def receive_alert(alert: SIEMAlert):
    """
    Receive a SIEM alert, normalize it, enrich the source IP,
    merge the results, and return the final enriched alert.
    """

    # ---------------------------------------------------------
    # 1. Alert received
    # ---------------------------------------------------------
    logger.info(
        "ALERT_RECEIVED id=%s ip=%s",
        alert.id,
        alert.src_ip,
    )

    # ---------------------------------------------------------
    # 2. Normalize incoming alert
    # ---------------------------------------------------------
    normalized = normalize_alert(
        alert.model_dump()
    )

    logger.info(
        "ALERT_NORMALIZED id=%s ip=%s",
        normalized["alert_id"],
        normalized["source_ip"],
    )

    # ---------------------------------------------------------
    # 3. Start threat intelligence enrichment
    # ---------------------------------------------------------
    logger.info(
        "ENRICHMENT_REQUEST id=%s ip=%s",
        normalized["alert_id"],
        normalized["source_ip"],
    )

    # ---------------------------------------------------------
    # 4. Perform threat intelligence lookup
    # ---------------------------------------------------------
    enrichment = check_ip_reputation(
        normalized["source_ip"]
    )

    # ---------------------------------------------------------
    # 5. Merge normalized alert + enrichment
    # ---------------------------------------------------------
    enriched_alert = merge_alert(
        normalized,
        enrichment,
    )

    # ---------------------------------------------------------
    # 6. Log final enriched alert
    # ---------------------------------------------------------
    logger.info(
        "ALERT_ENRICHED id=%s ip=%s reputation_score=%s source=%s",
        enriched_alert["alert_id"],
        enriched_alert["source_ip"],
        enriched_alert["enrichment"].get("reputation_score"),
        enriched_alert["enrichment"].get("source"),
    )

    logger.info(
        "FINAL_ALERT_READY id=%s",
        enriched_alert["alert_id"],
    )

    # ---------------------------------------------------------
    # 7. Return final API response
    # ---------------------------------------------------------
    return {
        "status": "received",
        "enriched_alert": enriched_alert,
        "message": "Alert received and enriched successfully",
    }
