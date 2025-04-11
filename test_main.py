import pytest
import httpx # this is the HTTP client library we use to simulate HTTP requests to our FastAPI app
from main import app  # imports the FastAPI app from your main.py
from httpx import ASGITransport #this lets httpx.AsyncClient talk directly to the FastAPI app in memory, without needing to start a real server.
from yfinance import Ticker as real_Ticker

@pytest.mark.asyncio #tells pytest this is an async test function.
async def test_get_stock(monkeypatch): #the test function itself. We pass monkeypatch from pytest to mock yfinance.
    # Mocked data that resembles yfinance output
    mock_info = {
        "shortName": "Mock Corp",
        "currentPrice": 123.45,
        "regularMarketChangePercent": 2.34,
        "volume": 1000000
    }

    class MockTicker:
        def __init__(self, ticker):
            self.ticker = ticker
            self.info = mock_info

    # Monkeypatch yfinance.Ticker to return the mock
    monkeypatch.setattr("yfinance.Ticker", MockTicker) #This line replaces yfinance.Ticker with our MockTicker class just for this test.

    # Use ASGITransport for FastAPI app
    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/stocks/FAKE") #Parse the response body as JSON so we can inspect the values.
    
    assert response.status_code == 200 #Check that the server responded with HTTP 200 OK.
    result = response.json()
    
    # These are all the assertions to make sure your /stocks/FAKE route returns the expected fields and values from the mocked yfinance data.
    assert result["ticker"] == "FAKE"
    assert result["shortName"] == "Mock Corp"
    assert result["price"] == 123.45
    assert result["change"] == 2.34
    assert result["volume"] == 1000000
