

from Roasted_Corn4_Function_Class import sample_Data_Of_Longest_Words

from unittest import TestCase

class Roasted_Corn4_Test_Function(TestCase):
    def test_Longest_Words(self):
        myWord = []
        longest_Word = sample_Data_Of_Longest_Words(myWord)
        max_Length = sample_Data_Of_Longest_Words(myWord)

        self.assertTrue(longest_Word, max_Length)
