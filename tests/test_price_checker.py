import unittest
from app.price_checker import get_price

class TestPrices(unittest.TestCase):
    def test_valid_symbol(self):
        self.assertEqual(get_price("BTC"),58000)
        
    def test_invalid_symbol(self):
        self.assertEqual(get_price("XYZ"),"Symbol not found")
        
if __name__ == "__main__":
    unittest.main()
