"""Day 11 of 2021 Advent of Code"""

import numpy as np

file = open('inputs/input11.txt')
text = file.read()

octopus = np.array(list(map(lambda x: [int(i) for i in x], text.split('\n'))))


# First problem

def flash(levels, x, y, flashes):
    levels[x][y] = 0
    flashes.append((x, y))

    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if (i, j) not in flashes and i >= 0 and j >= 0:
                try:
                    levels[i][j] += 1
                    if levels[i][j] > 9:
                        flash(levels, i, j, flashes)
                except IndexError:
                    continue


def do_step(levels):
    flashes = []
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            levels[i][j] += 1

    for i in range(len(levels)):
        for j in range(len(levels[0])):
            if levels[i][j] > 9:
                flash(levels, i, j, flashes)

    return len(flashes)


print(sum([do_step(octopus) for i in range(100)]))


# Second problem

day = 100
while octopus.any():
    do_step(octopus)
    day += 1

print(day)
