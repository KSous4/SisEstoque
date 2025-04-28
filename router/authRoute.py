from fastapi import APIRouter, Depends, Request
from fastapi.responses import Response,JSONResponse,RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from http import HTTPStatus
from schemas.Token import Token
from db.database import getDB
from handlers.loginhandler import loginHander

authRoute = APIRouter()


@authRoute.post('/login', response_model=Token)
async def login(response:Response,
                 request: Request,
                 form: OAuth2PasswordRequestForm=Depends(),
                 db=Depends(getDB)):
    return loginHander(request, response ,db, form.email, form.password,)
    