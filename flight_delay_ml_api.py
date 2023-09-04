# Libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import sklearn
import joblib

app = FastAPI()

class FlightInfo(BaseModel):
  arrstn: int
  depstn: int
  std: int
  sta: int

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