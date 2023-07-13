from fastapi import APIRouter, HTTPException
from app.api.models import SensorCreate, SensorUpdate
from app.db.models import Sensor

router = APIRouter()