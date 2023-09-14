from fastapi import APIRouter, HTTPException
from schemas.flight_info import FlightInfo
import pandas as pd
from config import settings  # Import application settings
from utils.model_loader import load_model
# from utils.data_preprocessing import preprocess_data

router = APIRouter()

model = load_model(settings.MODEL_PATH)

@router.post('/predict')
async def predict_flight_delay(input_data: FlightInfo):
    try:
        # preprocessed_data = preprocess_data([input_data])
        df = pd.DataFrame([input_data.model_dump().values()], columns=input_data.model_dump().keys())
        y_pred = model.predict(df)
        return {"prediction": int(y_pred)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    