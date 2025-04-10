from fastapi import FastAPI
import yfinance as yf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stocks/{ticker}")
async def get_stock(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.info
    # print('data', data)
    # print(data.get("shortName"))
    return {
        "ticker": ticker,
        "shortName": data.get("shortName"),
        "price": data.get("currentPrice"),
        "change": data.get("regularMarketChangePercent"),
        "volume": data.get("volume")
    }

# Expected return format JSON:
# {
# ticker: "GOOG",
# shortName: "Google Inc",
# price: 159.68,
# change: 8.940507,
# volume: 32479473
# }

# https://yfinance-python.org
