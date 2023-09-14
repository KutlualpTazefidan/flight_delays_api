from pydantic import BaseSettings

class Settings(BaseSettings):
    ALLOWED_ORIGINS: list = ["*"]
    MODEL_PATH: str = "app/models/api_test_logistic_regression_model.joblib"

settings = Settings()