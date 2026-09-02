from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Portfolio"
    environment: str = "development"
    debug: bool = True

    frontend_url: str = "http://localhost:5173"

    openrouter_api_key: str = ""
    openrouter_model: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()