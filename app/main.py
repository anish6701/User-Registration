from fastapi import FastAPI
# from app.auth import router as auth_router
from auth import router as auth_router  
from database import Base, engine

from fastapi.staticfiles import StaticFiles



app = FastAPI(title="User Registration")
app.mount("/static", StaticFiles(directory="static"), name="static")
# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Register the user API
app.include_router(auth_router)
