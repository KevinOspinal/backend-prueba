from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"❌ HTTPException: {exc.detail} (status {exc.status_code})")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception(f"🔥 Unexpected error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error"},
    )
