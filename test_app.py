import unittest
from app import calculate_monthly_food

class TestCalculateMonthlyFood(unittest.TestCase):

    def test_calculate_monthly_food(self):
        # Test for correct results
        result = calculate_monthly_food(3, 1, 4, 15)
        self.assertEqual(result, 186)

    def test_negative_monthly_food(self):
        # Test that if order is negative, result is 0
        result = calculate_monthly_food(0, 0, 0, 100)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()