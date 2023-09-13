from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.flight_info import FlightInfo
import sklearn
import joblib
import pandas as pd
from config import settings  # Import application settings
from utils.model_loader import load_model

router = APIRouter()

model = load_model(settings.MODEL_PATH)

@router.post('/predict/')
async def predict_flight_delay(input_data: FlightInfo):
    try:
        df = pd.DataFrame([input_data.model_dump().values()], columns=input_data.model_dump().keys())
        y_pred = model.predict(df)
        return {"prediction": int(y_pred)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    