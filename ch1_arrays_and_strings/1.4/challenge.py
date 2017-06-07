def is_string_permutation_palindrome(s):
	# First run through: 
	# To be a palindrome, the string must satisfy one of these conditions:
	# 	1. There are an even number of all non-whitespace characters
	# 	2. There are an even number of all but one non-white space characters
	
	# Get count of all characters
	chars = {}
	for c in ''.join(s.split()).lower(): # Runs in O(n); n = length of s
		if c in chars:
			chars[c] += 1
		else:
			chars[c] = 1

	# Get count of non-even characters
	odds = 0
	for c in chars:
		if chars[c] % 2 != 0:
			odds += 1

	if odds > 1:
		return False

	return True


if __name__ == "__main__":
	is_string_permutation_palindrome(raw_input())
