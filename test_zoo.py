import unittest
from zooticketcalculator import Zoo

class TestZooTicketCalculator(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_negative_age(self):
        self.assertIsNone(self.zoo.get_ticket_price(-5))

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()