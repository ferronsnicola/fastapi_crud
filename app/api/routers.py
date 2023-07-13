from fastapi import APIRouter, HTTPException
from app.api.models import SensorCreate, SensorUpdate
from app.db.models import Sensor

router = APIRouter()
SessionLocal = None

@router.post("/sensors/", status_code=201)
def create_sensor(sensor: SensorCreate):
    # TODO
    return None

@router.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: int):
    # TODO
    return None

@router.put("/sensors/{sensor_id}")
def update_sensor(sensor_id: int, sensor: SensorUpdate):
    # TODO
    return None

@router.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int):
    # TODO
    return None
