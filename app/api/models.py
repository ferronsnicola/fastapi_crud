from pydantic import BaseModel

class SensorCreate(BaseModel):
    name: str
    ip_address: str
    last_value: float

class SensorUpdate(BaseModel):
    name: str
    ip_address: str
    last_value: float
