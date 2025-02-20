from auth.authenticate import Authentication

from fastapi import Response,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from http import HTTPStatus
import logging


def authenticateUser(r: Response, formData: OAuth2PasswordRequestForm):

    # must have to implements the getUsr method to get user data from db
    usr: dict = getUsr(formData.username)
    if not usr or formData.password != usr['passwd']:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail="Invalid credentials")

    token = Authentication.create_acess_token(data={'sub': formData.username})

    r.set_cookie(
        key='accessToken',
        value=token,
        httponly=True,
        max_age=20,
        secure=True,
        samesite='lax'
    )

    return JSONResponse(
        content={'message': 'Logged successfully'}, status_code=HTTPStatus.OK
    )
