

from Roasted_Corn5_Function_Class import odd_Word
from unittest import TestCase

class Roasted_Corn5_Test_Function(TestCase):

    def test_odd_Word(self):
#        vowel_Words = ["semicolon"]
        vowel_Words = " "
        myWord = odd_Word(vowel_Words)
#        vowels = odd_Word(vowel_Words)
        self.assertTrue(myWord)

