"""Day 16 of 2020 Advent of Code"""

file = open('./input16.txt')
text = file.read()

lines = text.split('\n\n')


def make_rules(x):
    vals = list(map(lambda n: n.split('-'), x.split(': ')[1].split(' or ')))
    return list(map(lambda n: list(map(int, n)), vals))


rules = list(map(make_rules, lines[0].split('\n')))
tickets = list(map(lambda x: list(map(int, x)),
                   list(map(lambda x: x.split(','), lines[2].split('\n')[1:]))))


# First problem

def valid_field(value):
    for rule in rules:
        for val in rule:
            if value in range(val[0], val[1] + 1):
                return True
    return False


invalids = []
for ticket in tickets:
    for field in ticket:
        if not valid_field(field):
            invalids.append(field)

print(sum(invalids))


# Second problem

