# Schema
from pydantic import BaseModel

class FlightInfo(BaseModel):
    id: str
    datop: str
    fltid: str
    depstn: str
    arrstn: str
    std: str
    sta: str
    status: str
    ac: str
    dep_iata: str
    dep_country: str
    dep_elevation: float
    dep_lat: float
    dep_lon: float
    arr_iata: str
    arr_country: str
    arr_elevation: float
    arr_lat: float
    arr_lon: float

