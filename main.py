from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router=router)


@app.get("/hello")
def hello_world():
    return "Hello World"