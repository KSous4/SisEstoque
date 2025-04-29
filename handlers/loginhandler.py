from db.database import getDB
from fastapi import Depends,Request
from fastapi.responses import Response, RedirectResponse
from sqlalchemy.orm import Session
from schemas.userSchema import User
from utils.encriptation import verify_password
from security.security import AuthUser
from http import HTTPStatus
from datetime import time



def loginHander(request: Request,response: Response, db: Session, email: str, passwd: str):

    user = AuthUser(db,email,passwd)

    if not user:
        return Response(HTTPStatus.UNAUTHORIZED)
    
    access_token_expires = timedelta(minutes=authSecurity.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authSecurity.create_access_token(
        data={"sub": user.username,"role":user.is_Admin}, expires_delta=access_token_expires
    )
    response = RedirectResponse(url="/index",status_code=status.HTTP_302_FOUND)

    # to save token in cookie
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True) 
    return response