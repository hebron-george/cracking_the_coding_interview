def zero_matrix(m):
	# Initial solution:
	zero_coords = get_zero_locations(m)
	return zero_row_column(zero_coords, m)


def get_zero_locations(m):
	# m has dimension: M x N
	M = len(m)
	N = len(m[0])
	zero_coords = []
	for i in range(M):
		for j in range(N):
			if m[i][j] == 0:
				zero_coords.append([i,j])

	return zero_coords

def zero_row_column(coords, m):
	M = len(m)
	N = len(m[0])
	for c in coords:
		for i in range(N):
			m[c[0]][i] = 0
		for i in range(M):
			m[i][c[1]] = 0
	return m


if __name__ == "__main__":
	zero_matrix(eval(raw_input()))
