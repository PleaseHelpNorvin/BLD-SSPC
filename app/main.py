from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers import 

app = FastAPI()

# Mount static files (CSS/JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers (controllers)
app.include_router(HomeController.router)