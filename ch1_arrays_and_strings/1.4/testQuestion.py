import unittest
import challenge


class TestQuestion(unittest.TestCase):

	def setUp(self):
		pass

	def test_perm_is_not_palindrome(self):
		e = False
		a = challenge.is_string_permutation_palindrome("asdf")

		self.assertEquals(a, e)

	def test_tacocat(self):
		e = True
		a = challenge.is_string_permutation_palindrome("Tact Coa")

		self.assertEquals(a, e)

	def test_malayalam(self):
		e = True
		a = challenge.is_string_permutation_palindrome("malayalam")

		self.assertEquals(a, e)

	def test_not_a_palindrome(self):
		e = False
		a = challenge.is_string_permutation_palindrome("Not a Palindrome")

		self.assertEquals(a, e)


if __name__ == "__main__":
	unittest.main()