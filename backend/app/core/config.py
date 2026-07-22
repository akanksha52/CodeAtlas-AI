from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    api_version: str

    llm_provider: str = "ollama"

    ollama_model: str
    ollama_host: str

    gemini_model: str = "gemini-2.5-flash"

    groq_api_key: Optional[str] = Field(
        default=None,
        alias="GROQ_API_KEY"
    )

    gcp_api_key: Optional[str] = Field(
        default=None,
        alias="GCP_API_KEY"
    )

    groq_model: str = "llama-3.3-70b-versatile"

    embedding_model: str = "nomic-embed-text"

    retrieval_threshold: float = 1.1

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        populate_by_name=True,
    )
    
    frontend_origin: str = Field(
    default="http://localhost:5173",
    alias="FRONTEND_ORIGIN"
    )


settings = Settings()