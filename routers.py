from fastapi import APIRouter
from config import settings

currency_api_key = settings.ALPHA_VANTAGE_API_KEY

router = APIRouter()


@router.get("/converter/{from_currency}")
def converter(from_currency: str, to_currencies: str, price: float):
    print(from_currency)
    print(currency_api_key)
    return "hello"