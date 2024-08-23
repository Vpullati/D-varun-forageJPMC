import unittest
from datafeed import get_stock_data

class TestGetStockData(unittest.TestCase):
    
    def test_valid_symbols(self):
        # Test for valid symbols
        bid_price, ask_price = get_stock_data("AAPL")
        self.assertGreater(bid_price, 150)
        self.assertGreater(ask_price, 150)
    
    def test_invalid_symbol(self):
        # Test for an invalid symbol
        result = get_stock_data("INVALID")
        self.assertEqual(result, (0, 0))

if __name__ == "__main__":
    unittest.main()
