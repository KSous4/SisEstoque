#from database.SisEstoqueDB import Database
#from router.authRoutes import AuthRoute
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from http import HTTPStatus

mainRoute = APIRouter()

templates = Jinja2Templates(directory='templates')

@mainRoute.get("/ping")
async def healthCheck():
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={'status': 'pong'})

@mainRoute.get('/')
async def root(request: Request):
    return templates.TemplateResponse('./login/login.html', {'request':request})

#mainRoute.include_router(AuthRoute)
