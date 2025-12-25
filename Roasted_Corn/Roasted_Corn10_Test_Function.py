
from Roasted_Corn10_Function_Class import string_And_Number
from unittest import TestCase

class Roasted_Corn10_Test_Function(TestCase):
    def test_string_And_Number(self):
        numbers = "."
        words = " "
        myValue = string_And_Number(words, numbers)
        self.assertTrue(myValue)
        




#
#
#    myWord = []
#        longest_Word = sample_Data_Of_Longest_Words(myWord)
#        max_Length = sample_Data_Of_Longest_Words(myWord)
#
#        self.assertTrue(longest_Word, max_Length)
