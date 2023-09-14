# Libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import predict_flight_delay,preprocess_data
from config import settings  # Import application settings

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

@app.get('/')
def info_message():
    return "API to estimate flight delays, available routes: /prediction /preprocessdata"

# Include the prediction router
app.include_router(predict_flight_delay.router, prefix="/predict")
app.include_router(preprocess_data.router, prefix="/preprocessdata")