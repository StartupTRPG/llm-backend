from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 