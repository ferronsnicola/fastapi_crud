from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.models import Base
from app.api.routers import router as api_router
import app.api.routers as routers

# Create the FastAPI app
app = FastAPI()

# SQLAlchemy database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
routers.SessionLocal = SessionLocal

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api")