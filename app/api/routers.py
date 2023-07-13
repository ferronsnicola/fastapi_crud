from fastapi import APIRouter, HTTPException
from app.api.models import SensorCreate, SensorUpdate
from app.db.models import Sensor

router = APIRouter()
SessionLocal = None

@router.post("/sensors/", status_code=201)
def create_sensor(sensor: SensorCreate):
    db = SessionLocal()
    new_sensor = Sensor(name=sensor.name, ip_address=sensor.ip_address, last_value=sensor.last_value)
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor

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
