from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.auth.router import router as auth
from backend.app.owner.router import router as owner
from backend.app.upload.router import router as upload

app = FastAPI()


origins = [
    "http://localhost:5173",   
    "http://localhost:5174",   
    "http://192.168.1.105:5173",
    "https://c643c7910866.ngrok-free.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth)
app.include_router(owner)
app.include_router(upload)