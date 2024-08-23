import unittest
from datafeed import get_stock_data

class TestGetStockData(unittest.TestCase):
    
    def test_valid_symbols(self):
        # Test that the function returns a price within the expected range for valid symbols
        self.assertGreater(get_stock_data("AAPL"), 150)
        self.assertLess(get_stock_data("AAPL"), 200)
        self.assertGreater(get_stock_data("MSFT"), 250)
        self.assertLess(get_stock_data("MSFT"), 300)
        self.assertGreater(get_stock_data("GOOG"), 2700)
        self.assertLess(get_stock_data("GOOG"), 2800)
        self.assertGreater(get_stock_data("TSLA"), 700)
        self.assertLess(get_stock_data("TSLA"), 900)

    def test_invalid_symbol(self):
        # Test that the function returns the correct message for invalid symbols
        self.assertEqual(get_stock_data("INVALID"), "Symbol not found")

if __name__ == '__main__':
    unittest.main()
