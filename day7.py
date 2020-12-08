"""Day 7 of 2020 Advent of Code"""

file = open('./input7.txt')
text = file.read()

lines = text.split('\n')

bags = {}
for i in lines:
    name = i.split(' contain ')[0][:-5]
    content = i.split(' contain ')[1].split(', ')

    new_content = []
    for x in range(len(content)):
        if 'other' in content[x]:
            content.clear()
        else:
            aux = content[x].split()
            new_content.append((int(aux[0]), f'{aux[1]} {aux[2]}'))

    bags[name] = new_content


# First problem

def find_sons(color):
    return list(map(lambda c: c[1], bags[color]))


def find_parents(color):
    colors = []
    for col in bags.keys():
        if color in find_sons(col):
            colors.append(col)

    return colors


parents, new_parents = set(), set(find_parents('shiny gold'))
while parents != new_parents:
    parents = new_parents
    for i in parents:
        new_parents = new_parents.union(set(find_parents(i)))

print(len(new_parents))


# Second problem

def find_numbers(color):
    return list(map(lambda c: c[0], bags[color]))


def get_sons(color):
    count = 1

    if not bags[color]:
        return 1
    else:
        for col, num in zip(find_sons(color), find_numbers(color)):
            count += num * get_sons(col)
    return count


print(get_sons('shiny gold') - 1)
