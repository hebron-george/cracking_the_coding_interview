import collections

def compress_string(s):
	# Initial run through:
	char_to_compare = s[0]
	char_count = 0

	all_chars_and_counts = []
	for char in s:
		if char_to_compare != char:
			all_chars_and_counts.append((char_to_compare, char_count))
			char_to_compare = char
			char_count = 1
		else:
			char_count += 1
	all_chars_and_counts.append((char_to_compare, char_count))

	compressed_str = ''
	for x, y in all_chars_and_counts:
		compressed_str += x + str(y)

	if len(compressed_str) >= len(s):
		return s

	return compressed_str


if __name__ == "__main__":
	compress_string(raw_input())
