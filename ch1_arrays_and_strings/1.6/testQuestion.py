import unittest
import challenge


class TestQuestion(unittest.TestCase):


	def test_same_length_compression(self):
		e = "aabbcc"
		a = challenge.compress_string("aabbcc")

		self.assertEquals(a, e)

	def test_crappy_compression(self):
		e = "abc"
		a = challenge.compress_string("abc")

		self.assertEquals(a, e)

	def test_triples_compression(self):
		e = "a3b3c3"
		a = challenge.compress_string("aaabbbccc")

		self.assertEquals(a, e)

	def test_given_sample(self):
		e = 'a2b1c5a3'
		a = challenge.compress_string("aabcccccaaa")

		self.assertEquals(a, e)


if __name__ == "__main__":
	unittest.main()
