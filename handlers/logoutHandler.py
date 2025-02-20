from fastapi import Response
from fastapi.responses import JSONResponse
from http import HTTPStatus
import logging


def unAuthenticateUser(r: Response):

    r.delete_cookie('accessToken')

    return JSONResponse(
        content={'message': 'Logged Out'}, status_code=HTTPStatus.OK
    )
