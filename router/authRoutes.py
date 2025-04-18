from fastapi import APIRouter
from fastapi import Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
#from database.SisEstoqueDB import Database
from sqlmodel import Session
#from utils.databaseDependency import get_db_session
from handlers.loginHandler import authenticateUser
from handlers.logoutHandler import unAuthenticateUser
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

AuthRoute = APIRouter()


#@AuthRoute.post('/login')
#async def login(formData: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db_session)):
#    logger.warning(f"Received username: {formData.username}")
#    logger.warning(f"Received password: {formData.password}")
##  
##   # Call the authenticateUser function
##   return await authenticateUser(formData, session)
#

@AuthRoute.post('/logout')
async def logout(r: Response):
    return await unAuthenticateUser(r)
