import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        expected_prices = {'ABC': 120.84, 'DEF': 119.775}  # Calculated average of bid and ask prices
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, expected_prices[stock])


    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        expected_prices = {'ABC': 119.84, 'DEF': 119.775}  # Calculated average of bid and ask prices
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, expected_prices[stock])


    """ ------------ More unit tests ------------ """
    def test_getRatio(self):
        # Test when price_b is not zero
        price_a = 120.0
        price_b = 110.0
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, price_a / price_b)
        
        # Test when price_b is zero (Check for ZeroDivisionError)
        price_a = 120.0
        price_b = 0.0
        ratio = getRatio(price_a, price_b)
        self.assertIsNone(ratio)


if __name__ == '__main__':
    unittest.main()
