from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):

    app_name: str
    api_version: str
    frontend_origin: str

    llm_provider: str = "ollama"

    ollama_model: str
    ollama_host: str

    gemini_model: str = "gemini-2.5-flash"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GCP_API_KEY = os.getenv("GCP_API_KEY")
    groq_model: str = "llama-3.3-70b-versatile"

    embedding_model: str = "nomic-embed-text"
    
    retrieval_threshold: float = 1.1

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()