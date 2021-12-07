"""Day 1 of 2020 Advent of Code"""

file = open('inputs/input1.txt')
text = file.read()

numbers = list(map(int, text.split('\n')))
sort_numbers = numbers
sort_numbers.sort()


# First problem

# # Option 1: O(n^2) compexity
for i in numbers:
    if 2020 - i in numbers:
        print(i * (2020-i))
        break

# # Option 2: O(n) with sorted list
x, y = 0, len(sort_numbers) - 1
for i in range(y):
    if sort_numbers[x] + sort_numbers[y] < 2020:
        x += 1
    elif sort_numbers[x] + sort_numbers[y] > 2020:
        y -= 1
    else:
        print(sort_numbers[x] * sort_numbers[y])
        break


# Second problem

# # Option 1: O(n^3) compexity
i, found = 0, False
while i < len(numbers) and not found:
    x = 2020 - numbers[i]
    for j in numbers:
        if x - j in numbers:
            print(numbers[i] * j * (2020 - numbers[i] - j))
            found = True
            break
    i += 1

# # Option 2: O(n^2) compexity with sorted list
x, y, z = 0, 1, len(sort_numbers) - 1
for i in range(z*z):
    if sort_numbers[x] + sort_numbers[y] + sort_numbers[z] == 2020:
        print(sort_numbers[x] * sort_numbers[y] * sort_numbers[z])
        break
    if sort_numbers[x] + sort_numbers[y] + sort_numbers[z] < 2020:
        y += 1
    elif sort_numbers[x] + sort_numbers[y] + sort_numbers[z] > 2020 and y != x + 1:
        x, y = x + 1, x + 2
    else:
        x, y, z = 0, 0, z - 1
