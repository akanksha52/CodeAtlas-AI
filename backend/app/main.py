from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.core.logging import logger
from app.core.config import settings
from app.api.index import router as index_router
from app.api.stats import router as stats_router
from app.api.tree import router as tree_router
from app.core.dependencies import index_manager
from app.api.file import router as file_router
from app.api.explain import router as explain_router

app = FastAPI(title=settings.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    index_manager.build("sample_repo")
    
app.include_router(chat_router, prefix="/api/v1",)
app.include_router(health_router)
app.include_router(index_router, prefix=f"/api/{settings.api_version}", tags=["Index"],)
app.include_router(stats_router, prefix=f"/api/{settings.api_version}", tags=["Stats"],)
app.include_router(tree_router, prefix=f"/api/{settings.api_version}", tags=["Repository"],)
app.include_router(file_router, prefix=f"/api/{settings.api_version}", tags=["Repository"],)
app.include_router(explain_router, prefix=f"/api/{settings.api_version}", tags=["Repository"],)

logger.info("=" * 60)
logger.info(settings.app_name)
logger.info(f"Provider   : {settings.llm_provider}")
if settings.llm_provider.lower() == "gemini":
    logger.info(f"Model      : {settings.gemini_model}")
else:
    logger.info(f"Model      : {settings.ollama_model}")
logger.info(f"API Version: {settings.api_version}")
logger.info("=" * 60)