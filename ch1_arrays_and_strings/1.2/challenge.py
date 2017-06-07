def isPermutation(s1, s2):
	if set(s1) == set(s2):
		return True
	return False

if __name__ == "__main__":
	isPermutation(raw_input(), raw_input())
