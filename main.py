# Libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import flight_prediction
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
    return "API to estimate flight delays, available routes: /prediction"

# Include the prediction router
app.include_router(flight_prediction.router, prefix="/prediction")