"""Day 13 of 2020 Advent of Code"""

file = open('inputs/input14.txt')
text = file.read()

lines = text.split('mask = ')
list_instructions = list(map(lambda x: x.split('\n')[:-1], lines[1:]))


def simplify(instrs):
    return list(map(lambda x: (int(x[4:].split('] = ')[0]), int(x[4:].split('] = ')[1]))
                    if 'mem' in x else x, instrs))


instructions = list(map(simplify, list_instructions))


# First problem

def put_mask(number, mask):
    binary = bin(number)[2:]
    binary = '0' * (len(mask) - len(binary)) + binary

    masked = ''
    for b, m in zip(binary, mask):
        masked += b if m == 'X' else '1' if m == '1' else '0'

    return int(masked, 2)


memory = {}
for instruction in instructions:
    for i in range(1, len(instruction)):
        memory[instruction[i][0]] = put_mask(instruction[i][1], instruction[0])

print(sum(memory.values()))


# Second problem

def get_mems(memmask, mems):
    if 'X' not in memmask:
        mems.append(int(memmask, 2))
    else:
        get_mems(memmask.replace('X', '0', 1), mems)
        get_mems(memmask.replace('X', '1', 1), mems)


def mem_mask(slot, mask):
    binary = bin(slot)[2:]
    binary = '0' * (len(mask) - len(binary)) + binary

    masked, mems = '', []
    for b, m in zip(binary, mask):
        masked += b if m == '0' else '1' if m == '1' else 'X'

    get_mems(masked, mems)
    return mems


memory = {}
for instruction in instructions:
    for i in range(1, len(instruction)):
        for mem in mem_mask(instruction[i][0], instruction[0]):
            memory[mem] = instruction[i][1]

print(sum(memory.values()))
