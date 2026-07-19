from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    app_name: str
    api_version: str
    frontend_origin: str

    llm_provider: str = "ollama"

    ollama_model: str
    ollama_host: str

    gemini_model: str = "gemini-2.5-flash"
    gemini_api_key: str = ""

    embedding_model: str = "nomic-embed-text"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()