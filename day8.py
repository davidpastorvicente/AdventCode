"""Day 8 of 2020 Advent of Code"""

file = open('./input8.txt')
text = file.read()

lines = text.split('\n')
instructions = list(map(lambda x: [x.split()[0], int(x.split()[1])], lines))


# First problem

def good_game(instrs):
    index, accum, hist = 0, 0, []
    while index not in hist:
        hist.append(index)
        if instrs[index][0] == 'nop':
            index += 1
        elif instrs[index][0] == 'jmp':
            index += instrs[index][1]
        elif instrs[index][0] == 'acc':
            accum += instrs[index][1]
            index += 1

        if index == len(instrs) - 1:
            return True, accum
    return False, accum


print(good_game(instructions)[1])


# Second problem

nops, jumps = [], []
for i in range(len(instructions)):
    if instructions[i][0] == 'nop':
        nops.append(i)
    elif instructions[i][0] == 'jmp':
        jumps.append(i)

for i in nops:
    instructions[i][0] = 'jmp'
    result = good_game(instructions)
    if result[0]:
        print(result[1])

    instructions[i][0] = 'nop'

for i in jumps:
    instructions[i][0] = 'nop'
    result = good_game(instructions)
    if result[0]:
        print(result[1])

    instructions[i][0] = 'jmp'
