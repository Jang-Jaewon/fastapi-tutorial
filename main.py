from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router=router)


@app.get("/converter/{from_currency}")
def hello_world(from_currency: str, to_currencies: str, price: float):
    print(from_currency)
    print(to_currencies)
    print(price)
    return "It works"