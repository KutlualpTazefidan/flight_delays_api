import pandas as pd
from fastapi import APIRouter, HTTPException
from schemas.flight_info import FlightInfo
from pipelines_for_ml.preprocessing.flight_data.flight_data_complete_preprocessing import create_preprocessing_pipeline
import logging  # Import the logging module
# Configure the logging settings
logging.basicConfig(level=logging.ERROR)  # Set the logging level to DEBUG
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/preprocessdata')
async def preprocess_data(input_data: FlightInfo):
    try:
        # Create a dictionary from the FlightInfo object
        data_dict = input_data.model_dump()

        # Convert the dictionary to a DataFrame with a single row
        df = pd.DataFrame([data_dict])
        flight_prep_pipeline = create_preprocessing_pipeline()
        preprocessed_data = flight_prep_pipeline.transform(df)

        return {"preprocessed": preprocessed_data}
    except Exception as e:
        logger.error(f"Error in load_preprocessing_pipeline: {str(e)}")
        raise
