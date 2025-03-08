from router.router import mainRoute
from fastapi import FastAPI


app = FastAPI()



app.include_router(mainRoute)
