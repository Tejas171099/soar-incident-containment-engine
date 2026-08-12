import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("SOAR-Ingestion")


def log_alert_received(alert_id: str, source_ip: str):
    logger.info(
        f"[ALERT_RECEIVED] AlertID={alert_id} SourceIP={source_ip}"
    )


def log_enrichment_started(source_ip: str):
    logger.info(
        f"[ENRICHMENT_STARTED] SourceIP={source_ip}"
    )


def log_enrichment_completed(source_ip: str, reputation_score: int):
    logger.info(
        f"[ENRICHMENT_COMPLETED] SourceIP={source_ip} ReputationScore={reputation_score}"
    )


def log_enrichment_failed(source_ip: str, reason: str):
    logger.error(
        f"[ENRICHMENT_FAILED] SourceIP={source_ip} Reason={reason}"
    )
