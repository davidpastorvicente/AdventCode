"""Day 20 of 2020 Advent of Code"""

file = open('inputs/input20.txt')
text = file.read()

lines = text.split('\n\n')
tiles = {int(i.split(':')[0].split()[1]): i.split(':')[1].split('\n')[1:] for i in lines}
print(tiles)
