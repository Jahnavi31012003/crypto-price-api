def get_price(symbol):
    mock_data={
        "BTC":58000,
        "ETH":3000,
        "DOGE":0.09
    }
    return mock_data.get(symbol.upper(),"Symbol not found")
