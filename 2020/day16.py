"""Day 16 of 2020 Advent of Code"""

file = open('./input16.txt')
text = file.read()

lines = text.split('\n\n')


def make_rules(x):
    vals = list(map(lambda n: n.split('-'), x.split(': ')[1].split(' or ')))
    return list(map(lambda n: list(map(int, n)), vals))


rules = list(map(make_rules, lines[0].split('\n')))
my_ticket = list(map(int, lines[1].split('\n')[1].split(',')))
tickets = list(map(lambda x: list(map(int, x)),
                   list(map(lambda x: x.split(','), lines[2].split('\n')[1:]))))


# First problem

def valid_field_all(value):
    for rule in rules:
        for val in rule:
            if value in range(val[0], val[1] + 1):
                return True
    return False


invalid_fields, invalid_tickets = [], []
for ticket in tickets:
    for field in ticket:
        if not valid_field_all(field):
            invalid_fields.append(field)
            invalid_tickets.append(ticket)

print(sum(invalid_fields))


# Second problem

def valid_field(value, rule):
    for val in rule:
        if value in range(val[0], val[1] + 1):
            return True
    return False


def valid_column(col, rule):
    for val in col:
        if not valid_field(val, rule):
            return False
    return True


for ticket in invalid_tickets:
    tickets.remove(ticket)

aux = {}
for i in range(len(tickets[0])):
    aux[i] = []
    for j in range(len(rules)):
        if valid_column([x[i] for x in tickets], rules[j]):
            aux[i].append(j)


def del_value(val, cols):
    for col in cols:
        if val in aux[col]:
            aux[col].remove(val)


aux = {k: v for k, v in sorted(aux.items(), key=lambda x: len(x[1]))}
keys = list(aux.keys())
for i in range(len(keys) - 1):
    del_value(aux[keys[i]][0], keys[i+1:])

aux = {v[0]: k for k, v in aux.items()}
num = 1
for i in range(6):
    num *= my_ticket[aux[i]]

print(num)
