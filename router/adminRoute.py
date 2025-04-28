from fastapi import APIRouter, Request
from handlers. userHandler import createUser

adminRoute = APIRouter()

@adminRoute.post('/createUser')
async def createAdmin(req:Request):
    body = await req.json()
    return createUser(name=body['name'],email=body['email'], passwd=body['passwd'])
