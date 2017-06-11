import unittest
import challenge


class TestQuestion(unittest.TestCase):

	def test_rotated_1x1(self):
		e = [['a']]
		a = challenge.rotate_matrix([['a']])

		self.assertEquals(a, e)

	def test_rotated_2x2(self):
		e = [['c','a'], ['d','b']]
		a = challenge.rotate_matrix([['a', 'b'],['c', 'd']])

		self.assertEquals(a, e)

	def test_rotated_3x3(self):
		e = [['g', 'd', 'a'],['h', 'e', 'b'], ['i', 'f', 'c']]
		a = challenge.rotate_matrix([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])

		self.assertEquals(a, e)


if __name__ == "__main__":
	unittest.main()
