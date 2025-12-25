
from Roasted_Corn2_Function_Class import new_Word
from unittest import TestCase


class Roasted_Corn2_Test_Function(TestCase):

    def test_new_Word(self):
        text = ["Semicolon", "on", "o"]

        newWord = new_Word(text) 
    
        self.assertTrue(newWord)
