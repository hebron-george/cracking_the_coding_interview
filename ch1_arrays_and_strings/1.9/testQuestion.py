import unittest
import challenge

class TestQuestion(unittest.TestCase):

	def test_waterbottle_rotation(self):
		e = True
		a = challenge.is_rotated('waterbottle', 'erbottlewat')

		self.assertEquals(a, e)

	def test_different_strings(self):
		e = False
		a = challenge.is_rotated('asdf', 'jkl;')

		self.assertEquals(a, e)

if __name__ == "__main__":
	unittest.main()
