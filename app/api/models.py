from pydantic import BaseModel

class Sensor(BaseModel):
    name: str
    ip_address: str
    last_value: float

