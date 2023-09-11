import unittest
from unittest.mock import patch
from app_inputs import calculate_monthly_food, get_positive_int_input

class TestCalculateMonthlyFood(unittest.TestCase):

    def test_calculate_monthly_food(self):
        # Test for correct results
        result = calculate_monthly_food(3, 1, 4, 15)
        self.assertEqual(result, 186)

    def test_negative_monthly_food(self):
        # Test that if order is negative, result is 0
        result = calculate_monthly_food(0, 0, 0, 100)
        self.assertEqual(result, 0)

class TestGetPositiveIntInput(unittest.TestCase):
    @patch('app_inputs.get_input', return_value='1')
    def test_get_positive_int_input(self, input):
        result = get_positive_int_input('Test Prompt')
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()