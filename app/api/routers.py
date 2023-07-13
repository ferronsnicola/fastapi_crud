from fastapi import APIRouter, HTTPException
from app.api.models import Sensor as ApiSensor
from app.db.models import Sensor as DbSensor

router = APIRouter()
SessionLocal = None

@router.post("/sensors/", status_code=201, description='Creates a new sensor data in the database, and returns it as a succesfull response')
def create_sensor(sensor: ApiSensor):
    db = SessionLocal()
    new_sensor = DbSensor(name=sensor.name, ip_address=sensor.ip_address, last_value=sensor.last_value)
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor

@router.get("/sensors/{sensor_id}", description='Retrieve sensor by ID, raises HttpException if there is no sensor with specified ID')
def get_sensor(sensor_id: int):
    db = SessionLocal()
    sensor = db.query(DbSensor).filter(DbSensor.id == sensor_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor

@router.put("/sensors/{sensor_id}", description='Updates the specified sensor fields according to the specified sensor ID, raises HttpException if there is no sensor with specified ID, return the modified sensor as succesfull response')
def update_sensor(sensor_id: int, sensor: ApiSensor):
    db = SessionLocal()
    existing_sensor = db.query(DbSensor).filter(DbSensor.id == sensor_id).first()
    if not existing_sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    existing_sensor.name = sensor.name
    existing_sensor.ip_address = sensor.ip_address
    existing_sensor.last_value = sensor.last_value
    db.commit()
    db.refresh(existing_sensor)
    return existing_sensor

@router.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int):
    # TODO
    return None
