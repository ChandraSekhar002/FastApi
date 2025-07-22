from pydantic import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = "your_api_key"
    DB_URL: str = "sqlite:///./test.db"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
