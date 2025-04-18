from router.router import mainRoute
from fastapi import FastAPI, Request
import logging
#from sqlalchemy import text
from fastapi.staticfiles import StaticFiles

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Initialize the database
#db = Database("postgresql+psycopg2://user:pass@localhost:5432/SisEstoque")

# Set the db_instance in databaseDependency.py
# db_instance = db

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
# Include the router
app.include_router(mainRoute)

# Print all routes for debugging
for route in app.routes:
    print(f"Route: {route.path}")