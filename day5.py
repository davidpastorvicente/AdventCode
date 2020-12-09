"""Day 5 of 2020 Advent of Code"""

import re

file = open('./input5.txt')
text = file.read()

lines = text.split('\n')


# First problem

lines = list(map(lambda x: re.sub(r'[BR]', '1', x), lines))
seats = list(map(lambda x: int(re.sub(r'[FL]', '0', x), 2), lines))

print(max(seats))


# Second problem

seats.sort()
for i in range(len(seats) - 1):
    if seats[i + 1] != seats[i] + 1:
        print(seats[i] + 1)
        break
