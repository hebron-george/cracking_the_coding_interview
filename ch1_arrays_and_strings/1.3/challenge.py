def urlify(string_to_urlify, last_index):
	s = string_to_urlify[0:int(last_index)]
	return s.replace(' ', "%20")

if __name__ == "__main__":
	urlify(raw_input(), raw_input())
