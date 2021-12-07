"""Day 18 of 2020 Advent of Code"""

file = open('inputs/input18.txt')
text = file.read()

expressions = text.split('\n')


# First problem

def evaluate(exp):
    vals, ops = [], []
    for i in exp:
        if i == ' ':
            continue
        elif i == '(':
            ops.append(i)
        elif i.isdigit():
            vals.append(i)
        elif i == ')':
            while len(ops) != 0 and ops[-1] != '(':
                vals.append(str(eval(vals.pop() + ops.pop() + vals.pop())))
            ops.pop()
        else:
            while len(ops) != 0 and ops[-1] != '(':
                vals.append(str(eval(vals.pop() + ops.pop() + vals.pop())))
            ops.append(i)

    while len(ops) != 0:
        vals.append(str(eval(vals.pop() + ops.pop() + vals.pop())))

    return vals[-1]


num = 0
for expression in expressions:
    num += int(evaluate(expression))

print(num)


# Second problem

def precedence(op):
    return 1 if op == '+' else 0


def evaluate_precedence(exp):
    vals, ops = [], []
    for i in exp:
        if i == ' ':
            continue
        elif i == '(':
            ops.append(i)
        elif i.isdigit():
            vals.append(i)
        elif i == ')':
            while len(ops) != 0 and ops[-1] != '(':
                vals.append(str(eval(vals.pop() + ops.pop() + vals.pop())))
            ops.pop()
        else:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(i) and ops[-1] != '(':
                vals.append(str(eval(vals.pop() + ops.pop() + vals.pop())))
            ops.append(i)

    while len(ops) != 0:
        vals.append(str(eval(vals.pop() + ops.pop() + vals.pop())))

    return vals[-1]


num = 0
for expression in expressions:
    num += int(evaluate_precedence(expression))

print(num)
