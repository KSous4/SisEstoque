from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse,RedirectResponse
from http import HTTPStatus

authRoute = APIRouter()


@authRoute.post('/login')
async def login():
    return RedirectResponse('/home', HTTPStatus.SEE_OTHER)
    