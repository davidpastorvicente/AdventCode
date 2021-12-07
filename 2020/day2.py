"""Day 2 of 2020 Advent of Code"""

file = open('inputs/input2.txt')
text = file.read()

lines = text.split('\n')


def get_data(line):
    rule = line.split(': ')[0]
    password = line.split(': ')[1]

    numbers = rule.split(' ')[0]
    letter = rule.split(' ')[1]

    number1 = int(numbers.split('-')[0])
    number2 = int(numbers.split('-')[1])

    return password, letter, number1, number2


# First problem

count = 0
for i in lines:
    pwd, let, n1, n2 = get_data(i)
    if pwd.count(let) in range(n1, n2 + 1):
        count += 1

print(count)


# Second problem

count = 0
for i in lines:
    pwd, let, n1, n2 = get_data(i)

    if pwd[n1 - 1] == let and pwd[n2 - 1] != let:
        count += 1
    elif pwd[n1 - 1] != let and pwd[n2 - 1] == let:
        count += 1

print(count)
