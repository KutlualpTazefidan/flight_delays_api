from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALLOWED_ORIGINS: list = ["*"]
    MODEL_PATH: str = "models/api_test_logistic_regression_model.joblib"

settings = Settings()