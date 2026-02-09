from fastapi import FastAPI
import os
import time
import random

SERVICE = os.getenv("SERVICE_NAME", "notifications-service")
app = FastAPI(title=SERVICE)

@app.get("/health")
def health():
    return {"service": SERVICE, "status": "ok"}

@app.post("/v1/notify")
def notify(to: str, message: str):
    time.sleep(random.uniform(0.01, 0.06))
    return {"sent": True, "to": to, "message": message, "service": SERVICE}
