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

# Optional: known domain names for mapping logos
company_domains = {
    "AAPL": "apple.com",
    "GOOG": "google.com",
    "MSFT": "microsoft.com",
    "AMZN": "amazon.com",
    "META": "meta.com",
}

@app.get("/stocks/{ticker}")
async def get_stock(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.info
    # print('data', data)
    # print(data.get("shortName"))
        # Default to Clearbit logo if domain is known
    domain = company_domains.get(ticker.upper())
    logo_url = f"https://logo.clearbit.com/{domain}" if domain else None
    
    return {
        "ticker": ticker,
        "shortName": data.get("shortName"),
        "price": data.get("currentPrice"),
        "change": data.get("regularMarketChangePercent"),
        "volume": data.get("volume"),
        "logo": logo_url
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
