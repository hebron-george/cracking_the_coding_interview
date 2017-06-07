import unittest
import challenge


class TestQuestion(unittest.TestCase):

	def setUp(self):
		pass

	def test_with_duplicates(self):
		expected = False
		actual = challenge.has_all_unique_characters("aabbcc")

		self.assertEqual(actual, expected)

	def test_with_unique(self):
		e = True
		a = challenge.has_all_unique_characters('abc')

		self.assertEqual(a, e)


if __name__ == "__main__":
	unittest.main()
