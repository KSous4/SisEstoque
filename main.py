from router.router import mainRoute
from database.SisEstoqueDB import Database
from models.userModel import Users
from fastapi import FastAPI, Request
import logging
from sqlalchemy import text
from utils.databaseDependency import get_db_session, db_instance

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize the database
db = Database("postgresql+psycopg2://user:pass@localhost:5432/SisEstoque")

# Set the db_instance in databaseDependency.py
db_instance = db

app = FastAPI()

# Include the router
app.include_router(mainRoute)

# Print all routes for debugging
for route in app.routes:
    print(f"Route: {route.path}")