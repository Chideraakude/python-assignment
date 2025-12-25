
from Roasted_Corn9_Function_Class import find_Total_Of_Square_Of_Numbers
from unittest import TestCase

class Roasted_Corn9_Test_Function(TestCase):

    def test_find_Total_Of_Square_Of_Numbers(self):
        total = []
        numbers = find_Total_Of_Square_Of_Numbers(total)
        self.assertNotEqual(numbers, total)
