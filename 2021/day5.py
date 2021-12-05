"""Day 5 of 2021 Advent of Code"""
import numpy as np

file = open('./input5.txt')
text = file.read()

vectors = list(map(lambda x: list(map(lambda y: tuple(map(int, y.split(','))), x.split(' -> '))), text.split('\n')))

size = max(max(max(vectors)))
board = np.empty((size+1, size+1))


# First problem

def get_range(ini, end):
    return range(ini, end+1) if end > ini else range(ini, end-1, -1)


def add_vector(brd, vect):
    a, b = vect

    if a[0] == b[0]:
        for i in get_range(a[1], b[1]):
            brd[a[0]][i] += 1

    if a[1] == b[1]:
        for i in get_range(a[0], b[0]):
            brd[i][a[1]] += 1


for v in vectors:
    add_vector(board, v)

print((board > 1).sum())


# Second problem

def add_diagonal(brd, vect):
    a, b = vect

    if a[0] != b[0] and a[1] != b[1]:
        for i, j in zip(get_range(a[0], b[0]), get_range(a[1], b[1])):
            brd[i][j] += 1


for v in vectors:
    add_diagonal(board, v)

print((board > 1).sum())
