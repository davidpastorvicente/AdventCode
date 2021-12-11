"""Day 10 of 2021 Advent of Code"""

file = open('inputs/input10.txt')
text = file.read()

chunks = text.split('\n')


# First problem

delimiters = {')': '(', ']': '[', '}': '{', '>': '<'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

opens = delimiters.values()
closes = delimiters.keys()


def check_chunk(line):
    queue = []

    for i in line:
        if i in opens:
            queue.append(i)
        elif i in closes:
            if delimiters[i] == queue[-1]:
                queue.pop()
            else:
                return points[i], queue

    return 0, queue


print(sum([check_chunk(chunk)[0] for chunk in chunks]))


# Second problem

points_2 = {'(': 1, '[': 2, '{': 3, '<': 4}


def calc_points(queue):
    num_points = 0
    for i in reversed(queue):
        num_points *= 5
        num_points += points_2[i]
    return num_points


aux = []
for chunk in chunks:
    errors, spares = check_chunk(chunk)
    if errors == 0:
        aux.append(calc_points(spares))

aux.sort()
print(aux[len(aux)//2])
