from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String

Base = declarative_base()

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    ip_address = Column(String(50))
    last_value = Column(Float)