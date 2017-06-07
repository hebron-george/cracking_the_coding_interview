def has_all_unique_characters(string):
	# First thought: go through each character, 
	# update a dictionary where key = character, value = count

	# Second thought: As soon as we see a character in the dictionary already,
	# the function can return false. This stays at O(n) run time since if we have a 
	# completely unique set of characters (worst case), we'll have to go through them all anyway, 
	# but returns false at the first instance of a duplicate character.

	# Third thought: using a list instead of a dictionary to save space

	# Fourth thought: If we can't use additional data structures, we can get the length of the input
	# which is a O(1) operation, and get the length of the set(input), also a O(1) operation

	if len(string) > len(set(string)):
		return False
	return True

if __name__ == "__main__":
	has_all_unique_characters(raw_input())
