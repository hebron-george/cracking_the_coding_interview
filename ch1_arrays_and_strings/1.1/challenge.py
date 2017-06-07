def has_all_unique_characters(string):
	# First thought: go through each character, 
	# update a dictionary where key = character, value = count

	character_dictionary = {}
	for c in string: # This should have a runtime of O(n) where n = size of string
		if c in character_dictionary:
			character_dictionary[c] += 1
		else:
			character_dictionary[c] = 1

	for key in character_dictionary:
		if character_dictionary[key] > 1:
			return False

	return True

if __name__ == "__main__":
	has_all_unique_characters(raw_input())
