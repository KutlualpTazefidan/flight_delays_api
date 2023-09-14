# Libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowPassword as OAuthFlowPasswordModel
from api.routes import predict_flight_delay,preprocess_data
from config import settings  # Import application settings

app = FastAPI()
app.debug = True

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
app.include_router(predict_flight_delay.router)
app.include_router(preprocess_data.router)

# Enable automatic documentation generation
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)