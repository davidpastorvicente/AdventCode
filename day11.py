"""Day 11 of 2020 Advent of Code"""

import numpy as np

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
    return (get_seat(row + 1, seat) + get_seat(row, seat + 1) +
            get_seat(row - 1, seat) + get_seat(row, seat - 1) +
            get_seat(row + 1, seat + 1) + get_seat(row + 1, seat - 1) +
            get_seat(row - 1, seat + 1) + get_seat(row - 1, seat - 1))


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

rows = np.array(list(map(list, lines)))


def find_occupied(seats, reverse=False):
    seats = np.flip(seats) if reverse else seats

    for i in seats:
        if i != '.':
            return 1 if i == '#' else 0
    return 0


def diag_adjacents(seats, row, seat):
    if seat > row:
        return find_occupied(seats.diagonal(seat - row)[:row], True) + \
               find_occupied(seats.diagonal(seat - row)[row + 1:])

    else:
        return find_occupied(seats.diagonal(seat - row)[:seat], True) + \
               find_occupied(seats.diagonal(seat - row)[seat + 1:])


def new_num_adjacents(row, seat):
    adjs = 0
    adjs += find_occupied(rows[row][:seat], True) + find_occupied(rows[row][seat + 1:])
    adjs += find_occupied(rows[:, seat][:row], True) + find_occupied(rows[:, seat][row + 1:])
    adjs += diag_adjacents(rows, row, seat)
    adjs += diag_adjacents(np.fliplr(rows), row, num_seats - 1 - seat)

    return adjs


prev_rows = []
while not np.array_equal(rows, prev_rows):
    prev_rows = rows
    rows = np.array(do_iteration(5, new_num_adjacents))

print(np.count_nonzero(rows == '#'))
