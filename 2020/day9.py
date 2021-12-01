"""Day 9 of 2020 Advent of Code"""

file = open('./input9.txt')
text = file.read()

lines = text.split('\n')
numbers = list(map(int, lines))


# First problem

def is_valid(number, index):
    preamble = numbers[index-25: index]

    for n in preamble:
        if number - n in preamble and n != number - n:
            return True
    return False


wrong = 0
for i, num in enumerate(numbers):
    if i >= 25 and not is_valid(num, i):
        wrong = num
        print(wrong)
        break


# Second problem

ini, end, sol = 0, 0, []
while sum(sol) != wrong:
    if sum(sol) < wrong:
        sol.append(numbers[end])
        end += 1
    elif sum(sol) > wrong:
        ini += 1
        end = ini + 1
        sol = [numbers[ini]]

print(min(sol) + max(sol))
