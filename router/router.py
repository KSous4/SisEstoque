#from router.authRoutes import AuthRoute

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

mainRoute = APIRouter()


@mainRoute.get("/ping")
async def healthCheck():
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={'status': 'pong'})


#mainRoute.add_route(route=AuthRoute)
