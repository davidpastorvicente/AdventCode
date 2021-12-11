"""Day 9 of 2021 Advent of Code"""

import numpy as np

file = open('inputs/input9.txt')
text = file.read()

heights = np.array(list(map(lambda x: [int(i) for i in x], text.split('\n'))))


# First problem

def get_adjacents(values, x, y):
    adjs = []
    if x > 0:
        adjs.append(values[x-1][y])
    if x < len(values)-1:
        adjs.append(values[x+1][y])
    if y > 0:
        adjs.append(values[x][y-1])
    if y < len(values[0])-1:
        adjs.append(values[x][y+1])
    return adjs


def check_low(values, x, y):
    if all(adj > values[x][y] for adj in get_adjacents(values, x, y)):
        return values[x][y] + 1
    return 0


num = 0
for i in range(len(heights)):
    for j in range(len(heights[0])):
        num += check_low(heights, i, j)

print(num)
