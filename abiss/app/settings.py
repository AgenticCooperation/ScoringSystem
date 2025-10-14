from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://postgres:password@localhost:5432/abiss_db"
    
    # CORS
    allow_origins: List[str] = ["*"]
    
    # Telemetry
    telemetry_schema_version: str = "1.0"
    
    # Application
    app_name: str = "ABISS - Advanced Backend Intelligence Scoring System"
    app_version: str = "1.0.0"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
