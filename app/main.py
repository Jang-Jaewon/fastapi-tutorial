from fastapi import FastAPI

from app.routers.category_routers import router as category_router
from app.routers.poc import router as poc_router
from app.routers.product_routers import router as product_router
from app.routers.user_routers import router as user_router

app = FastAPI()


@app.get("/health-check")
def health_check():
    return True


app.include_router(category_router)
app.include_router(product_router)
app.include_router(user_router)
app.include_router(poc_router)
