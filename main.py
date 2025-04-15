from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "LineAlert Config Server is running"}

@app.post("/api/init")
async def init_config(request: Request):
    body = await request.json()
    device_id = body.get("device_id", "unknown")
    hostname = body.get("hostname", "unknown")
    timestamp = datetime.utcnow().isoformat() + "Z"

    config = {
        "device_id": device_id,
        "hostname": hostname,
        "timestamp": timestamp,
        "update_available": False,
        "allowed_function_codes": [3, 4, 5]
    }

    print(f"[+] INIT: {device_id} ({hostname}) checked in at {timestamp}")
    return JSONResponse(content=config)
