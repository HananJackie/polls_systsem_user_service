from fastapi import FastAPI
from app.controller.user_controller import router as user_router
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/users", tags=["Users"])
