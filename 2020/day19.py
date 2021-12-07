"""Day 19 of 2020 Advent of Code"""

import re

file = open('inputs/input19.txt')
text = file.read()

lines = text.split('\n\n')


def make_dict():
    aux = {}
    for i in lines[0].split('\n'):
        key = int(i.split(': ')[0])
        value = list(map(lambda x: list(map(lambda y: int(y) if y.isdigit() else y[1],
                                            x.split())), i.split(': ')[1].split(' | ')))
        aux[key] = value

    return aux


rules = make_dict()
messages = lines[1].split('\n')


# First problem

def find_match(rule):
    if rule[0][0] == 'a' or rule[0][0] == 'b':
        return rule[0][0]
    else:
        pattern = ''
        for exp in rule:
            for i in exp:
                pattern += '(' + find_match(rules[i]) + ')'
            pattern += '|'
        return pattern[:-1]


num, pat = 0, find_match(rules[0])
for msg in messages:
    num += 1 if re.fullmatch(pat, msg) else 0

print(num)

# Second problem

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]


def find_match_loop(num_rule, reps):
    rule = rules[num_rule]

    if rule[0][0] == 'a' or rule[0][0] == 'b':
        return rule[0][0]
    else:
        pattern = r''
        for exp in rule:
            for i in exp:
                if num_rule == 8 or num_rule == 11:
                    reps += 1
                    if reps > 50:
                        continue

                pattern += '(' + find_match_loop(i, reps) + ')'
            pattern += '|'
        return pattern[:-1]


num, pat = 0, find_match_loop(0, 0)
for msg in messages:
    num += 1 if re.fullmatch(pat, msg) else 0

print(num)
