# models.py
from pydantic import BaseModel

class FlightInfo(BaseModel):
    departure_airport: str
    departure_city: str
    departure_country: str
    departure_time: str
    arrival_airport: str
    arrival_city: str
    arrival_country: str
    arrival_time: str
    airline: str
