"""Day 3 of 2020 Advent of Code"""

file = open('./input3.txt')
text = file.read()

lines = text.split('\n')
length = len(lines[0])


def count_trees(right, bottom):
    count, j = 0, 0
    for i in range(0, len(lines) - bottom, bottom):
        j += right
        if lines[i + bottom][j % length] == '#':
            count += 1
    return count


# First problem

print(count_trees(3, 1))


# Second problem

print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) *
      count_trees(7, 1) * count_trees(1, 2))
