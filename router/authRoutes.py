from fastapi import APIRouter
from fastapi import Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from handlers.loginHandler import authenticateUser
from handlers.logoutHandler import unAuthenticateUser


AuthRoute = APIRouter()


AuthRoute.post('/login')
async def login(r: Response, formData: OAuth2PasswordRequestForm = Depends()):
    return await authenticateUser(r, formData)

AuthRoute.post('/logout')
async def logout(r: Response):
    return await unAuthenticateUser(r)
