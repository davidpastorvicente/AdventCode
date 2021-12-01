"""Day 11 of 2020 Advent of Code"""

file = open('./input11.txt')
text = file.read()

lines = text.split('\n')
rows = list(map(list, lines))

num_rows = len(rows)
num_seats = len(rows[0])


# First problem

def get_seat(row, seat):
    if row < 0 or row >= num_rows or seat < 0 or seat >= num_seats:
        return 0
    else:
        return 1 if rows[row][seat] == '#' else 0


def num_adjacents(row, seat):
    adjs = 0
    dirs = [-1, 0, 1]
    for i in dirs:
        for j in dirs:
            if not (i == 0 and j == 0):
                adjs += get_seat(row + i, seat + j)

    return adjs


def do_iteration(limit, get_adjacents):
    new_rows = []
    for i in range(num_rows):
        new_seats = []
        for j in range(num_seats):
            if rows[i][j] == '.':
                new_seats.append('.')
            elif rows[i][j] == 'L':
                new_seats.append('#' if get_adjacents(i, j) == 0 else 'L')
            elif rows[i][j] == '#':
                new_seats.append('L' if get_adjacents(i, j) >= limit else '#')
        new_rows.append(new_seats)
    return new_rows


prev_rows = []
while rows != prev_rows:
    prev_rows = rows
    rows = do_iteration(4, num_adjacents)

num = 0
for rw in rows:
    num += rw.count('#')

print(num)


# Second problem

rows = list(map(list, lines))


def find_adjacent(row, seat, i, j):
    if row < 0 or row >= num_rows or seat < 0 or seat >= num_seats or rows[row][seat] == 'L':
        return 0
    else:
        return 1 if rows[row][seat] == '#' else find_adjacent(row + i, seat + j, i, j)


def new_num_adjacents(row, seat):
    adjs = 0
    dirs = [-1, 0, 1]
    for i in dirs:
        for j in dirs:
            if not (i == 0 and j == 0):
                adjs += find_adjacent(row + i, seat + j, i, j)

    return adjs


prev_rows = []
while rows != prev_rows:
    prev_rows = rows
    rows = do_iteration(5, new_num_adjacents)

num = 0
for rw in rows:
    num += rw.count('#')

print(num)
