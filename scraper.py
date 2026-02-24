import yfinance as yf
import requests
from bs4 import BeautifulSoup

def get_realtime_data():
    try:
        res_thai = requests.get("https://api.chnwt.dev/thai-gold-api/latest")
        gold_data = res_thai.json()

        try:
            thai_price = gold_data["response"]["price"]["gold_bar"]["sell"]
        except KeyError:
            thai_price = gold_data["response"]["price"]["gold_bar"]["sell"]

        gold_spot = yf.Ticker("GC=F")
        world_price = gold_spot.history(period="1d")["Close"].iloc[-1]

        thb_ticker = yf.Ticker("USDTHB=X")
        exchange_rate = thb_ticker.history(period="1d")["Close"].iloc[-1]

        return {
            "thai": thai_price,
            "world": round(float(world_price), 2),
            "rate": round(float(exchange_rate), 2)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("Fetching data...")
    print(get_realtime_data())
