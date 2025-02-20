from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from http import HTTPStatus
import logging

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            verify_acess_token(request)
            response = await call_next(request)
            return response
        except HTTPException as e:

            logging.warning(f'Error in authMiddleware:\n {e}')
            return JSONResponse(
                content={"detail":e.detail},
                status_code=e.status_code
                )
        except Exception as e:
            return JSONResponse(
                content={'detail':str(e)},status_code=HTTPStatus.INTERNAL_SERVER_ERROR
            )