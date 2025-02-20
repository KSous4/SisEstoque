from router.authRoutes import AuthRoute

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

mainRoute = APIRouter


@mainRoute.get("/health")
async def healthCheck():
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={'status': 'Application running heatlthy'})


mainRoute.add_route(route=AuthRoute)
