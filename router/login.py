from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from http import HTTPStatus

loginRoute = APIRouter()


loginRoute.post('/login')
async def login(user: dict = Depends(authenticate_user)):
    session_id = create_session(user["user_id"])
    return JSONResponse(
        content={
            "message":"Logged in successully",
            "session_id":session_id
        },status_code=HTTPStatus.OK
    )