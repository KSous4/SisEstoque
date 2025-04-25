from fastapi import APIRouter, Request


adminRoute = APIRouter()



@adminRoute.post('/createUser')
async def createAdmin(req:Request):
    

    body = await req.json