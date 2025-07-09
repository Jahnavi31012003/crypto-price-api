from fastapi import FastAPI
from app.price_checker import get_price

app=FastAPI()

@app.get("/price/{symbol}")
def read_price(symbol: str):
    return {"symbol" :symbol.upper(),"price": get_price(symbol)}
