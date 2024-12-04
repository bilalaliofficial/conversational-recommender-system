from fastapi import FastAPI, HTTPException
from .routers import routers
from app.utils.exceptions import custom_http_exception_handler
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

for router in routers:
    app.include_router(router, prefix="/api")

app.add_exception_handler(HTTPException, custom_http_exception_handler)

@app.get('/')
async def welcome():
    logger.info("Welcome endpoint called")
    return {'data': 'Welcome to the Customer Recommendor System!'}