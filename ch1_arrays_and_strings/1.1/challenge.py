def has_all_unique_characters(string):
	# First thought: go through each character, 
	# update a dictionary where key = character, value = count

	# Second thought: As soon as we see a character in the dictionary already,
	# the function can return false. This stays at O(n) run time since if we have a 
	# completely unique set of characters (worst case), we'll have to go through them all anyway, 
	# but returns false at the first instance of a duplicate character.

	# Third thought: using a list instead of a dictionary to save space

	character_list = []
	for c in string: # This should have a runtime of O(n) where n = size of string
		if c in character_list:
			return False
		else:
			character_list.append(c)

	return True

if __name__ == "__main__":
	has_all_unique_characters(raw_input())
