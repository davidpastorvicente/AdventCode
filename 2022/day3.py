file = open('inputs/input3.txt')
text = file.read()[:-1]

rucksacks = text.split('\n')


def get_common(*args):
    common = list(set(args[0]).intersection(*args[1:]))[0]
    if common.islower():
        return ord(common[0]) - ord('a') + 1
    return ord(common[0]) - 38


# First part

def get_common_2(rucksack):
    size = len(rucksack) // 2
    return get_common(rucksack[:size], rucksack[size:])


commons = list(map(get_common_2, rucksacks))
print(sum(commons))


# Second part

new_rucksacks = list(zip(*[iter(rucksacks)] * 3))
new_commmons = list(map(lambda x: get_common(*x), new_rucksacks))
print(sum(new_commmons))
