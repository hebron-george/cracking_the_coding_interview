def is_one_edit_away(s1, s2):
	if s1 == s2: # 0 edits away
		return True

	if abs(len(s1)-len(s2)) > 1:
		return False

	if len(s1) == len(s2):
		replace_count = 0
		for i, c in enumerate(s1): # O(n) runtime to check each character replacement
			if s2[i] != c:
				replace_count += 1
		if replace_count > 1:
			return False

	return True

if __name__ == "__main__":
	is_one_edit_away(raw_input(), raw_input())
