"""Day 3 of 2021 Advent of Code"""

file = open('inputs/input3.txt')
text = file.read()

numbers = list(map(str, text.split('\n')))


# First problem

def add_number(num, res):
    for i in range(len(num)):
        aux = int(num[i])
        res[i] = res[i] + (1 if aux == 1 else -1)

    return res


size = len(numbers[0])
result = [0] * size
for number in numbers:
    result = add_number(number, result)

gamma = int(''.join(['1' if i >= 0 else '0' for i in result]), 2)
epsilon = ~gamma & (2 ** size - 1)

print(gamma*epsilon)


# Second problem

def rem_common(nums, index, most):
    ones, zeros = [], []
    for i in nums:
        (zeros, ones)[i[index] == '1'].append(i)

    if len(ones) == len(zeros):
        return ones if most else zeros
    return max([ones, zeros], key=len) if most else min([ones, zeros], key=len)


def get_rating(nums, most):
    rating = nums
    for i in range(size):
        rating = rem_common(rating, i, most)
        if len(rating) == 1:
            break

    return int(rating[0], 2)


oxygen = get_rating(numbers, True)
co2 = get_rating(numbers, False)
print(oxygen*co2)
