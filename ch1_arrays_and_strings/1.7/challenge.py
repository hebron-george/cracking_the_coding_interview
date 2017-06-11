def rotate_matrix(m):
	# Initial run through
	n = len(m) # this gives us the dimensions of the matrix => n x n
	return_matrix = [[0 for x in range(n)] for y in range(n)]

	for i in range(0, n):
		for j in range(0, n):
			return_matrix[j][(n-1)-i] = m[i][j]

	return return_matrix


if __name__ == "__main__":
	print rotate_matrix(eval(raw_input())) # trustworthy input so I can call eval()
