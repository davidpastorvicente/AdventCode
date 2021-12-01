"""Day 1 of 2020 Advent of Code"""

file = open('./input1.txt')
text = file.read()

numbers = list(map(int, text.split('\n')))


# First problem

num = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        num += 1

print(num)


# Second problem

num = 0
for i in range(3, len(numbers)):
    if sum(numbers[i-2:i+1]) > sum(numbers[i-3:i]):
        num += 1

print(num)
