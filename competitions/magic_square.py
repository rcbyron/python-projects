""" Creates a "magic square" 2d array (must be odd size) """


def make_square(m):
    matrix = [[0 for i in range(m)] for j in range(m)]
    i = m-1
    j = int(m/2)
    for n in range(1, m*m):
        matrix[i][j] = n
        if not matrix[(i+1) % m][(j+1) % m] and not (i is m-1 and j is m-1):
            i = (i+1) % m
            j = (j+1) % m
        else:
            i -= 1

    return matrix


def show(m):
    for line in m:
        print(line)
    print()

show(make_square(9))
