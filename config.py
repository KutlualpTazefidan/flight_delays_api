from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALLOWED_ORIGINS: list = ["*"]
    MODEL_PATH: str = "models/api_test_logistic_regression_model.joblib"
    PREPROCESSING_PIPELINE_PATH:str = "utils/preprocessing/pipeline_1/preprocessing_pipeline_imported_classes.joblib"

settings = Settings()