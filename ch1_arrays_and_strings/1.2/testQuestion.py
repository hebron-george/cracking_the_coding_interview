import unittest
import challenge


class TestQuestion(unittest.TestCase):
	
	def setUp(self):
		pass

	def test_if_different_strings_are_permutation(self):
		e = False
		a = challenge.isPermutation("abc", "def")

		self.assertEqual(a, e)

	def test_if_same_chars_are_perm(self):
		e = True
		a = challenge.isPermutation("abc", "bac")

		self.assertEqual(a, e)

if __name__ == "__main__":
	unittest.main()