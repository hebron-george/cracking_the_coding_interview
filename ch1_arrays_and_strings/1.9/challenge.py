def is_rotated(s1, s2):
	# Initial solution: iterate through each character in s2 and pivot around it
	# if there's a match with s1, return True

	if len(s1) != len(s2):
		return False

	if s1 == s2:
		return True

	temp = s2
	for i in range(len(s2)):
		temp = temp[-1] + temp[0:len(temp)-1]
		if temp == s1:
			return True

	return False



if __name__ == "__main__":
	is_rotated(raw_input(), raw_input())
