from Roasted_Corn7_Function_Class import find_Maximum_Number
from unittest import TestCase

class Roasted_Corn7_Test_Function(TestCase):

    def test_find_Maximum_Number(self):
        numbers = " "
        maximum_Number = find_Maximum_Number(numbers)
        self.assertTrue(maximum_Number)
    
        
