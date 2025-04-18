from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from auth.authenticate import Authentication
#from models.userModel import Users
from http import HTTPStatus
from sqlmodel import select, Session 
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def authenticateUser(formData: OAuth2PasswordRequestForm, session: Session):
    stmt = select(Users).where(Users.username == formData.username)
    user = session.exec(stmt).first()
    
    if not user or formData.password != user.passwd:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = Authentication.create_access_token(data={'sub': formData.username})


    response = JSONResponse(
        content={'message': 'Logged in successfully'}, 
        status_code=HTTPStatus.OK
    )

    response.set_cookie(
        key='accessToken',
        value=token,
        httponly=True,
        max_age=30 * 60,
        secure=False,
        samesite='lax',
        path='/'
    )

    return response