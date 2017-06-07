import unittest
import challenge


class TestQuestion(unittest.TestCase):


	def setUp(self):
		pass

	def test_Mr_John_Smith(self):
		e = "Mr%20John%20Smith"
		a = challenge.urlify("Mr John Smith     ", 13)

		self.assertEquals(a, e)

	def test_string_with_no_spaces(self):
		e = "asdf"
		a = challenge.urlify("asdf", 4)

		self.assertEquals(a, e)


if __name__ == "__main__":
	unittest.main()