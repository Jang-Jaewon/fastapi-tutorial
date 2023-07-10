import requests
from config import settings
import aiohttp
from fastapi import HTTPException

ALPHAVANTAGE_APIKEY = settings.ALPHA_VANTAGE_API_KEY


def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}"
    try:
        response = requests.get(url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    data = response.json()

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(
            status_code=400, detail=f"Realtime Currency Exchange Rate not in response {data}"
        )

    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchange_rate


async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(
            status_code=400, detail=f"Realtime Currency Exchange Rate not in response {data}"
        )

    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchange_rate
