import random

def get_stock_data(symbol):
    """Simulate fetching stock data for a given symbol."""
    prices = {
        "AAPL": random.uniform(150, 200),
        "MSFT": random.uniform(250, 300),
        "GOOG": random.uniform(2700, 2800),
        "TSLA": random.uniform(700, 900),  # Added TSLA
    }
    return prices.get(symbol, "Symbol not found")

def main():
    # Simulate fetching data for different stocks
    symbols = ["AAPL", "MSFT", "GOOG", "TSLA"]
    for symbol in symbols:
        price = get_stock_data(symbol)
        if isinstance(price, str):
            print(f"The price of {symbol} is: {price}")
        else:
            print(f"The price of {symbol} is: {price:.2f}")

if __name__ == "__main__":
    main()
