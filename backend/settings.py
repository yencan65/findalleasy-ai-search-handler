from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    APP_NAME: str = "FindAllEasy AI Search Handler"
    DEBUG: bool = False
    TRENDYOL_API_KEY: str = Field(default="", env="TRENDYOL_API_KEY")
    CICEKSEPETI_API_KEY: str = Field(default="", env="CICEKSEPETI_API_KEY")
    AMAZON_API_KEY: str = Field(default="", env="AMAZON_API_KEY")
    BOOKING_API_KEY: str = Field(default="", env="BOOKING_API_KEY")
    OPENAI_API_KEY: str = Field(default="", env="OPENAI_API_KEY")
    TRANSLATE_API_KEY: str = Field(default="", env="TRANSLATE_API_KEY")
    COMMISSION_DEFAULT: float = 0.07
    COMMISSION_CAP_MIN: float = 0.02
    COMMISSION_CAP_MAX: float = 0.15
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
