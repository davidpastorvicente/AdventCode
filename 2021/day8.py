"""Day 8 of 2021 Advent of Code"""

file = open('inputs/input8.txt')
text = file.read()

patterns = list(map(lambda x: x.split(' | '), text.split('\n')))


# First problem

aux = list(map(lambda x: x[1].split(), patterns))
print(sum([sum(1 if len(i) in [2, 3, 4, 7] else 0 for i in pat) for pat in aux]))
