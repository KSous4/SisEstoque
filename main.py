from router.router import mainRoute
from database.SisEstoqueDB import Database
from fastapi import FastAPI
import logging
from sqlalchemy import text


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(mainRoute)

db = Database("postgresql+psycopg2://user:pass@localhost:5432/SisEstoque")

