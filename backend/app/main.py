from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.core.logging import logger
from app.core.config import settings
from app.services.index_manager import IndexManager

app = FastAPI(title=settings.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
index_manager = IndexManager()
index_manager.build("sample_repo")
app.include_router(chat_router, prefix="/api/v1",)
app.include_router(health_router)
logger.info("=" * 60)
logger.info(f"{settings.app_name}")
logger.info(f"Model      : {settings.ollama_model}")
logger.info(f"API Version: {settings.api_version}")
logger.info("=" * 60)