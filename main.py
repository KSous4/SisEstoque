from router.router import mainRoute
from db.database import Session
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(mainRoute)
