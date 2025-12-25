


from Roasted_Corn1_Function_Class import length_Calculator
from unittest import TestCase

class Roasted_Corn1_Test_Function(TestCase):

    def test_length_Calculator(self):
        sample_String = " "
        length = length_Calculator(sample_String)
        self.assertTrue(length)

