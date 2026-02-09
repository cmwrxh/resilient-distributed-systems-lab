from fastapi import FastAPI
import os
import time
import random

SERVICE = os.getenv("SERVICE_NAME", "user-service")
app = FastAPI(title=SERVICE)

@app.get("/health")
def health():
    return {"service": SERVICE, "status": "ok"}

@app.get("/v1/users/{user_id}")
def get_user(user_id: str):
    time.sleep(random.uniform(0.01, 0.05))
    return {"user_id": user_id, "name": "Charlie", "service": SERVICE}
