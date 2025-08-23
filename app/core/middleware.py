import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        logger.info(f"📥 Request: {request.method} {request.url}")

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        logger.info(
            f"📤 Response: status={response.status_code} "
            f"completed_in={process_time:.2f}ms"
        )

        return response
