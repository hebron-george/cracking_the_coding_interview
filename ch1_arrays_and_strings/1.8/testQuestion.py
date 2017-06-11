import unittest
import challenge

class TestQuestion(unittest.TestCase):

	def test_1x1(self):
		e = [[0]]
		a = challenge.zero_matrix([[0]])

		self.assertEquals(a, e)

	def test_3x2(self):
		e = [[1,0],[3,0],[0,0]]
		a = challenge.zero_matrix([[1,2],[3,4],[5,0]])

		self.assertEquals(a, e)

	def test_4x5(self):
		e = [[0,0,0,0,0],[0,0,0,0,0],[1,0,3,4,0],[1,0,3,4,0]]
		a = challenge.zero_matrix([[1,2,3,4,0],[1,0,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])

		self.assertEquals(a, e)



if __name__ == "__main__":
	unittest.main()
