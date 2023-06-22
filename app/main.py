from fastapi import FastAPI, Request
from time import time
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import analysis_report, auth, item, user

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/api/healthchecker")
def root():
    return {"message": "Hello World"}
