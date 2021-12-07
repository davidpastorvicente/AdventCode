"""Day 10 of 2020 Advent of Code"""

file = open('inputs/input10.txt')
text = file.read()

lines = text.split('\n')
numbers = list(map(int, lines))

numbers.append(0)
numbers.sort()
numbers.append(numbers[-1] + 3)


# First problem

ones, threes = 0, 0
for i in range(1, len(numbers)):
    if numbers[i] - numbers[i - 1] == 1:
        ones += 1
    elif numbers[i] - numbers[i - 1] == 3:
        threes += 1

print(ones * threes)


# Second problem

aux = {0: 1}
numbers.pop(0)
for number in numbers:
    aux[number] = 0
    if number - 1 in aux:
        aux[number] += aux[number - 1]
    if number - 2 in aux:
        aux[number] += aux[number - 2]
    if number - 3 in aux:
        aux[number] += aux[number - 3]

print(aux.popitem()[1])
