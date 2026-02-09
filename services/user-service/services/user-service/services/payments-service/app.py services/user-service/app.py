from fastapi import FastAPI, Header, HTTPException
import os
import time
import random

SERVICE = os.getenv("SERVICE_NAME", "payments-service")
app = FastAPI(title=SERVICE)

@app.get("/health")
def health():
    return {"service": SERVICE, "status": "ok"}

@app.post("/v1/payments/charge")
def charge(amount: float, idempotency_key: str | None = Header(default=None, alias="Idempotency-Key")):
    if not idempotency_key:
        raise HTTPException(status_code=400, detail="Missing Idempotency-Key header")
    time.sleep(random.uniform(0.02, 0.08))
    return {"charged": True, "amount": amount, "idempotency_key": idempotency_key, "service": SERVICE}
