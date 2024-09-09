from fastapi import APIRouter, Request
import uvicorn
from config import logger

route = APIRouter(
    prefix="/",
    dependencies="Template or Route",
)

route.get("/health")
def get_health(req: Request):
    logger.info(f"IP: {req.client.host} | Health")
    return {"message": "Healthy", "status_code": 200}

route.get("/getg")