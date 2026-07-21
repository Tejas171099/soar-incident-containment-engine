from fastapi import FastAPI

app = FastAPI(
    title="SOAR Incident Containment Engine",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "SOAR ingestion service is running"
    }
