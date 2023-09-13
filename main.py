# Libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import sklearn
import joblib

app = FastAPI()

# Configure CORS to allow requests from your Next.js app's domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class FlightInfo(BaseModel):
  departure_airport: str
  departure_city: str
  departure_country: str
  departure_time: str
  arrival_airport: str
  arrival_city: str
  arrival_country: str
  arrival_time:str
  airline:str
 
loaded_model = joblib.load("api_test_logistic_regression_model.joblib")

if isinstance(loaded_model, sklearn.base.BaseEstimator):
    model = loaded_model
else:
    raise ValueError("The loaded object is not a scikit-learn model.")

@app.post('/')
async def scoring_endpoint(item:FlightInfo):
    df = pd.DataFrame([item.model_dump().values()], columns = item.model_dump().keys() )
    y_pred = model.predict(df)
    return {"prediction":int(y_pred)}

@app.get('/')
def info_message():
    return "API to estimate flight delays"