from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    api_version: str
    frontend_origin: str
    ollama_model: str
    ollama_host: str
    embedding_model: str = "nomic-embed-text"
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()