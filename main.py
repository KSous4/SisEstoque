from router.router import mainRoute
from fastapi import FastAPI


app = FastAPI()



app.add_route(route=mainRoute)

