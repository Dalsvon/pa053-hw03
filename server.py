from fastapi import FastAPI
import requests
from typing import Optional

app = FastAPI()
keyYahoo = "164a1c4469mshc0a974eba4e4001p1d0f90jsn8a0b9724b1c6"
keyWeather = "587fe8bf7a9145cda5e14004252704"


def stockAPI(ticker):
    url = f"https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules"
    headers = {
        "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
        "x-rapidapi-key": keyYahoo
    }
    params = {
        "ticker": ticker,
        "module": "financial-data"
    }
    stock = requests.get(url, headers=headers, params=params)
    print(stock.json()["body"]["currentPrice"]["raw"])
    return stock.json()["body"]["currentPrice"]["raw"]

def airportAPI(code):
    url = "https://airport-data.com/api/ap_info.json"
    params = {
        "iata": code
    }
    airport = requests.get(url, params=params)
    return airport.json()["latitude"], airport.json()["longitude"]

def weatherAPI(latitude, longitude):
    location = str(latitude) + "," + str(longitude)
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "q": location,
        "key": keyWeather
    }
    weather = requests.get(url, params=params)
    return weather.json()["current"]["temp_c"]


@app.get("/")
async def get_data(queryAirportTemp: Optional[str] = None, queryStockPrice: Optional[str] = None, queryEval: Optional[str] = None):
    if queryAirportTemp:
        latitude, longitude = airportAPI(queryAirportTemp)
        return weatherAPI(latitude, longitude)
    if queryStockPrice:
        return stockAPI(queryStockPrice)
    if queryEval:
        return eval(queryEval)
    return -1