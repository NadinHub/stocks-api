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
        # Default to Clearbit logo if domain is known
    domain = company_domains.get(ticker.upper())
    
    logo_url = f"https://logo.clearbit.com/{domain}" if domain else None
    
    # Get historical prices
    hist = stock.history(period="5d", interval="1d")
   
    history = [
        {
            "time": date.strftime("%Y-%m-%d"), # frontend (light-weight) expects time (not date)
            "open": round(row["Open"], 2),
            "high": round(row["High"], 2),
            "low": round(row["Low"], 2),
            "close": round(row["Close"], 2),
            "volume": int(row["Volume"]),
        }
        for date, row in hist.iterrows()
    ]  
    
    return {
        "ticker": ticker,
        "shortName": data.get("shortName"),
        "price": data.get("currentPrice"),
        "change": data.get("regularMarketChangePercent"),
        "volume": data.get("volume"),
        "logo": logo_url,
        "history": history
    }

# Expected return format JSON:
# {
# ticker: "GOOG",
# shortName: "Google Inc",
# price: 159.68,
# change: 8.940507,
# volume: 32479473,
# history: [{},{}],
# }

# https://yfinance-python.org
