import random

def get_stock_data(symbol):
    """Simulate fetching stock data for a given symbol."""
    prices = {
        "AAPL": (random.uniform(150, 200), random.uniform(150, 200)),
        "MSFT": (random.uniform(250, 300), random.uniform(250, 300)),
        "GOOG": (random.uniform(2700, 2800), random.uniform(2700, 2800)),
        "TSLA": (random.uniform(700, 900), random.uniform(700, 900)),  # Added TSLA
    }
    return prices.get(symbol, (0, 0))  # Return tuple of (bid, ask)

def getDataPoint(stock_name, bid_price, ask_price):
    """Return a tuple of stock name, bid price, ask price, and average price."""
    price = (bid_price + ask_price) / 2
    return (stock_name, bid_price, ask_price, price)

def getRatio(price1, price2):
    """Return the ratio of two stock prices."""
    if price2 == 0:
        raise ValueError("Price2 cannot be zero.")
    return price1 / price2

def main():
    stock1 = "AAPL"
    stock2 = "MSFT"

    # Fetch simulated data
    bid_price1, ask_price1 = get_stock_data(stock1)
    bid_price2, ask_price2 = get_stock_data(stock2)

    # Get data points
    data1 = getDataPoint(stock1, bid_price1, ask_price1)
    data2 = getDataPoint(stock2, bid_price2, ask_price2)

    # Calculate ratio
    ratio = getRatio(data1[3], data2[3])

    # Output results
    print(f"Stock 1: {data1[0]}, Bid: {data1[1]:.2f}, Ask: {data1[2]:.2f}, Price: {data1[3]:.2f}")
    print(f"Stock 2: {data2[0]}, Bid: {data2[1]:.2f}, Ask: {data2[2]:.2f}, Price: {data2[3]:.2f}")
    print(f"Price Ratio (Stock 1 / Stock 2): {ratio:.2f}")

if __name__ == "__main__":
    main()
