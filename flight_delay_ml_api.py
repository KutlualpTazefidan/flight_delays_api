# Libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

class FlightInfo(BaseModel):
  arrstn: int
  depstn: int
  datop: int
  std_time: int

with open("api_test_logistic_regression_model.pkl",'rb') as f:
    model = pickle.load(f)

@app.post('/')
async def scoring_endpoint(item:FlightInfo):
    df = pd.DataFrame([item.dict().values], columns = item.dict().keys() )
    y_pred = model.predict(df)
    return {"prediction":int(y_pred)}