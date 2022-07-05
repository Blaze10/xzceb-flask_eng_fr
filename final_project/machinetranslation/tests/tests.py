import unittest
from machinetranslation import translator

class TestTranslator(unittest.TestCase):
    """
        Testing the translator module
    """

    def test_englishToFrench(self):
        """
            Test english to french translation
        """

        # raises ValueError is input is null
        with self.assertRaises(ValueError):
            translator.english_to_french(None)

        # Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')


    def test_frenchToEnglish(self):
        """
            Test french to english translation
        """

        # raises ValueError is input is null
        with self.assertRaises(ValueError):
            translator.french_to_english(None)

        # Test for the translation of the world 'Bonjour' and 'Hello'.
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello') #


unittest.main()