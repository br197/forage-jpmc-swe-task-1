import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
      self.assertEqual(getDataPoint(q), (q['stock'], q['top_bid']['price'],  q['top_ask']['price'], (q['top_bid']['price']+q['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
       self.assertEqual(getDataPoint(q), (q['stock'], q['top_bid']['price'],  q['top_ask']['price'], (q['top_bid']['price']+q['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceb_zero(self):
     price_a = 128
     price_b = 0
     self.assertEqual(getRatio(price_a, price_b), None)
  
  def test_getRatio_pricea_zero(self):
     price_a = 0
     price_b = 128
     self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_nonzero(self):
     price_a = 128
     price_b = 4
     self.assertEqual(getRatio(price_a, price_b), 32)



if __name__ == '__main__':
    unittest.main()
