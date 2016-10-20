""" Solves the "Eight Queens" problem """

QUEENS = 8
ROWS = 8
COLS = 8

chess = [[0 for x in range(COLS)] for x in range(ROWS)]


def reset():
    global chess
    chess = [[0 for x in range(COLS)] for x in range(ROWS)]


def show():
    for spot in chess:
        print(spot)
    print()


def in_bounds(row, col):
    if 0 <= row and row < ROWS and 0 <= col and col < COLS:
        return True
    return False


def check_dir(row, col, dx, dy):
    row += dx
    col += dy
    success = True
    if in_bounds(row, col):
        if chess[row][col] is 1:
            return False
        success = success and check_dir(row, col, dx, dy)
    return success


def can_put(row, col):
    global chess
    if chess[row][col] is 1:
        return False
    success = True
    success = success and check_dir(row, col, -1, -1)
    success = success and check_dir(row, col, -1, 1)
    success = success and check_dir(row, col, 1, -1)
    success = success and check_dir(row, col, 1, 1)
    success = success and check_dir(row, col, -1, 0)
    success = success and check_dir(row, col, 1, 0)
    success = success and check_dir(row, col, 0, -1)
    success = success and check_dir(row, col, 0, 1)
    return success


def place():
    global chess
    for row in range(ROWS):
        for col in range(COLS):
            if can_put(row, col):
                chess[row][col] = 1
                return True
    return False


def find():
    print("Finding matchess...")
    global chess
    for row in range(ROWS):
        for col in range(COLS):
            reset()
            chess[row][col] = 1
            fail = False
            for queen in range(QUEENS-1):
                if not place():
                    fail = True
                    break
            if not fail:
                show()
    print("Complete.")
find()
