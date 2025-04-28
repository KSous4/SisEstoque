from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2AuthorizationCodeBearer
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from http import HTTPStatus

from router.adminRoute import adminRoute
from router.authRoute import authRoute

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

mainRoute = APIRouter()

templates = Jinja2Templates(directory='templates')

@mainRoute.get("/ping")
async def healthCheck():
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={'status': 'pong'})

@mainRoute.get('/')
async def root(request: Request):
    return templates.TemplateResponse('./Login/login.html', {'request':request})


@mainRoute.get('/home')
async def home(request: Request):
    return templates.TemplateResponse('./Principal/principal.html', {'request':request})

mainRoute.include_router(adminRoute)
mainRoute.include_router(authRoute)