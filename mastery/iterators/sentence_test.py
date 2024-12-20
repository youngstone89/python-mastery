import unittest

from mastery.iterators.sentence import Sentence


class TestSentence(unittest.TestCase):

    def setUp(self):
        self.sentence = Sentence("Hello world! This is a test.")

    def test_init(self):
        self.assertEqual(self.sentence.text, "Hello world! This is a test.")

    def test_repr(self):
        expected = "Sentence('Hello world! This is a test.')"
        self.assertEqual(repr(self.sentence), expected)

    def test_iter(self):
        expected_words = ["Hello", "world", "This", "is", "a", "test"]
        self.assertEqual(list(self.sentence), expected_words)

    def test_empty_sentence(self):
        empty_sentence = Sentence("")
        self.assertEqual(list(empty_sentence), [])

    def test_sentence_with_punctuation(self):
        punctuated_sentence = Sentence("Hello, world! How are you?")
        expected_words = ["Hello", "world", "How", "are", "you"]
        self.assertEqual(list(punctuated_sentence), expected_words)


if __name__ == '__main__':
    unittest.main()
