


from Roasted_Corn8_Function_Class import find_Square_Of_Numbers
from unittest import TestCase

class Roasted_Corn8_Test_Function(TestCase):

    def test_find_Square_Of_Numbers(self):
        square_Of_Numbers = []
        square = find_Square_Of_Numbers(square_Of_Numbers)
        self.assertTrue(square)
