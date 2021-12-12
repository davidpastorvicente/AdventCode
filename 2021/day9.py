"""Day 9 of 2021 Advent of Code"""

import numpy as np

file = open('inputs/input9.txt')
text = file.read()

heights = np.array(list(map(lambda x: [int(c) for c in x], text.split('\n'))))


# First problem

def get_adjacents(values, x, y):
    adjs = []
    if x > 0:
        adjs.append((x-1, y))
    if x < len(values)-1:
        adjs.append((x+1, y))
    if y > 0:
        adjs.append((x, y-1))
    if y < len(values[0])-1:
        adjs.append((x, y+1))
    return adjs


def check_low(values, x, y):
    if all(values[adj[0]][adj[1]] > values[x][y] for adj in get_adjacents(values, x, y)):
        return values[x][y] + 1
    return 0


num = 0
for i in range(len(heights)):
    for j in range(len(heights[0])):
        num += check_low(heights, i, j)

print(num)


# Second problem

def get_basin(values, x, y, basin):
    adjs = get_adjacents(values, x, y)
    basin.add((x, y))

    for adj in adjs:
        if values[adj[0]][adj[1]] != 9 and values[adj[0]][adj[1]] > values[x][y]:
            get_basin(values, adj[0], adj[1], basin)

    return basin


basins = []
for i in range(len(heights)):
    for j in range(len(heights[0])):
        if check_low(heights, i, j):
            basins.append(get_basin(heights, i, j, set()))

basins.sort(key=len)
print(len(basins[-1]) * len(basins[-2]) * len(basins[-3]))
