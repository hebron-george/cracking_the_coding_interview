import unittest
import challenge


class TestQuestion(unittest.TestCase):

	def test_two_plus_inserts_away(self): # checks for 2+ inserts away
		e = False
		a = challenge.is_one_edit_away("hello wor", "hello world")

		self.assertEquals(a, e)

	def test_two_plus_removes_away(self):
		e = False
		a = challenge.is_one_edit_away("hello world", "hello wor")

		self.assertEquals(a, e)

	def test_two_plus_replacements_away(self):
		e = False
		a = challenge.is_one_edit_away("Hello World", "Hello Wordo")

		self.assertEquals(a, e)

	def test_ple_example(self):
		e = True
		a = challenge.is_one_edit_away("pale", "ple")

		self.assertEquals(a, e)

	def test_pales_example(self):
		e = True
		a = challenge.is_one_edit_away("pale", "pales")

		self.assertEquals(a, e)

	def test_bale_example(self):
		e = True
		a = challenge.is_one_edit_away("pale", "bale")

		self.assertEquals(a, e)

	def test_bake_example(self):
		e = False
		a = challenge.is_one_edit_away("pale", "bake")

		self.assertEquals(a, e)



if __name__ == "__main__":
	unittest.main()