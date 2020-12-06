"""Day 6 of 2020 Advent of Code"""

file = open('./input6.txt')
text = file.read()

lines = text.split('\n\n')
questions = list(map(lambda x: list(map(set, x.split('\n'))), lines))


# First problem

count = 0
for i in questions:
    count += len(i[0].union(*i[1:]))

print(count)


# Second problem

count = 0
for i in questions:
    count += len(i[0].intersection(*i[1:]))

print(count)
