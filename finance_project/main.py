"""Main module of Finance Application"""

from fastapi import FastAPI, HTTPException
from finance_project.schemas.stock_schemas import StockShema
from finance_project.models.stocks import Stock
from typing import List

app = FastAPI()

stocks: List[Stock] = [
    Stock("Apple Company", 102, "AAA.US"),
    Stock("Microsoft Company", 78, "MICRO.US"),
    Stock("Google Company", 92, "GGLE.US")
]

@app.get('/stocks')
def main():
    return stocks


@app.post("/stocks")
def add_stock(stock: StockShema):
    new_stock = Stock(**stock.model_dump())
    stocks.append(new_stock)


@app.get("/stocks/{stock_name}")
def get_stock_by_name(stock_name: str):
    for stock in stocks:
        if stock.name == stock_name:
            return stock
    raise HTTPException(status_code=404, detail="Stock not found")