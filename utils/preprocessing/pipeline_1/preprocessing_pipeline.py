import joblib
from config import settings  # Import application settings

def load_preprocessing_pipeline():
    # Load the preprocessing pipeline from the joblib file
    pipeline = joblib.load(settings.PREPROCESSING_PIPELINE_PATH)
    return pipeline