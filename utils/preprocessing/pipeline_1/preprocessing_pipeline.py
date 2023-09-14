import joblib
import logging  # Import the logging module
from config import settings  # Import application settings
from utils.preprocessing.pipeline_1.custom_classes import ColumnNameFixer, CalculateDistance, CustomFeaturesAdder, DropColumns, LabelEncoderTransformer

# Configure the logging settings
logging.basicConfig(level=logging.ERROR)  # Set the logging level to DEBUG

def load_preprocessing_pipeline():
    try:
        # Add a print statement to check the file path
        print("Loading preprocessing pipeline from:", settings.PREPROCESSING_PIPELINE_PATH)

        # Load the preprocessing pipeline from the joblib file
        pipeline = joblib.load(settings.PREPROCESSING_PIPELINE_PATH)
        return pipeline
    except Exception as e:
        # Log the error message if an exception is raised
        logging.error(f"Error in load_preprocessing_pipeline: {str(e)}")
        raise