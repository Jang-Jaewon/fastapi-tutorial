from fastapi import FastAPI
from routers import router

app = FastAPI()


app.include_router(router, tags=["TEST"], prefix="/api")


@app.get("/health")
def health_check():
    return "It works"
