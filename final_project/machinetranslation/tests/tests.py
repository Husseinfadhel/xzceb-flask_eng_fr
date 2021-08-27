import unittest
from translator import english_to_french, french_to_english


class TestFr(unittest.TestCase):
    

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_none(self):
        firstValue = None
        msg=None
        self.assertEqual(english_to_french('Text'), 'Texte')


class TestEn(unittest.TestCase):
    

    def test_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_none(self):
        firstValue = None
        msg=None
        self.assertEqual(french_to_english('Texte'), 'Text')


unittest.main()
