import joblib
import pandas as pd
from fastapi import APIRouter, HTTPException
from schemas.flight_info import FlightInfo
# from pydantic import BaseModel
from sklearn.base import BaseEstimator
from config import settings  # Import application settings
from utils.pipelines.model_loader import load_model
from pipelines_for_ml.preprocessing.flight_data.flight_data_complete_preprocessing import create_preprocessing_pipeline
import logging

# from utils.data_preprocessing import preprocess_data

router = APIRouter()

model = load_model(settings.MODEL_PATH)

# Configure the logging settings
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@router.post('/predict')
async def predict_flight_delay(input_data: FlightInfo):
    try:
        # Create a dictionary from the FlightInfo object
        data_dict = input_data.model_dump()

        # Convert the dictionary to a DataFrame with a single row
        df = pd.DataFrame([data_dict])
        flight_prep_pipeline = create_preprocessing_pipeline()
        preprocessed_data = flight_prep_pipeline.transform(df)
        
        loaded_model = joblib.load("pipelines_for_ml/ml_models/api_test_logistic_regression_model.joblib")
        if isinstance(loaded_model, BaseEstimator):
            model = loaded_model
        else:
            raise ValueError("The loaded object is not a scikit-learn model.")
        # preprocessed_data = preprocess_data([input_data])
        # df = pd.DataFrame([input_data.model_dump().values()], columns=input_data.model_dump().keys())
        y_pred = model.predict(preprocessed_data)
        return {"prediction": int(y_pred)}
    
    except Exception as e:
        # Log the error message if an exception is raised
        logging.error(f"Error in create_preprocessing_pipeline: {str(e)}")
        logger.error(f"Error in create_preprocessing_pipeline: {str(e)}")
        raise
        # raise HTTPException(status_code=500, detail=str(e))
    