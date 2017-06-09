import collections

def compress_string(s):
	# Initial run through:
	char_to_compare = ''
	character_count = collections.OrderedDict() # OrderedDict remembers insertion order
	for char in s:
		if char not in character_count.keys():
			character_count[char] = 1

		if char == char_to_compare:
			character_count[char] += 1
		else:
			char_to_compare = char
	
	compressed_str = ''
	for k in character_count:
		compressed_str += k + str(character_count[k])

	if len(compressed_str) >= len(s):
		return s

	return compressed_str


if __name__ == "__main__":
	compress_string(raw_input())
