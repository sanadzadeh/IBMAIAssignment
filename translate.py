import unittest
import deep_translator

def translate_english_to_french(text):
  translator = deep_translator.MyMemoryTranslator()
  translated_text = translator.translate(text, "en", "fr")
  return translated_text

def translate_french_to_english(text):
  translator = deep_translator.MyMemoryTranslator()
  translated_text = translator.translate(text, "fr", "en")
  return translated_text

class TestEnglishToFrench(unittest.TestCase):
  def test_translate_english_to_french(self):
    self.assertEqual(translate_english_to_french("Code for peer review"), "Code de révision par les pairs")
    self.assertNotEqual(translate_english_to_french("Code for peer review"), "Code for peer review")

class TestFrenchToEnglish(unittest.TestCase):
  def test_translate_french_to_english(self):
    self.assertEqual(translate_french_to_english("Code de révision par les pairs"), "Code for peer review")
    self.assertNotEqual(translate_french_to_english("Code de révision par les pairs"), "Code de révision par les pairs")

if __name__ == "__main__":
  unittest.main()
