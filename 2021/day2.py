"""Day 2 of 2021 Advent of Code"""

file = open('inputs/input2.txt')
text = file.read()

directions = list(map(lambda x: x.split(), text.split('\n')))


# First problem

position, depth = 0, 0
for direction in directions:
    if direction[0] == 'down':
        depth += int(direction[1])
    if direction[0] == 'up':
        depth -= int(direction[1])
    if direction[0] == 'forward':
        position += int(direction[1])

print(position * depth)


# Second problem

aim, position, depth = 0, 0, 0
for direction in directions:
    if direction[0] == 'down':
        aim += int(direction[1])
    if direction[0] == 'up':
        aim -= int(direction[1])
    if direction[0] == 'forward':
        position += int(direction[1])
        depth += aim * int(direction[1])

print(position * depth)
