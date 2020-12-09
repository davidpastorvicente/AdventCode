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

def change_instruction(instruction):
    if instruction == 'acc':
        return instruction
    else:
        return 'jmp' if instruction == 'nop' else 'nop'


for i in range(len(instructions)):
    instructions[i][0] = change_instruction(instructions[i][0])
    result = good_game(instructions)
    if result[0]:
        print(result[1])
        break

    instructions[i][0] = change_instruction(instructions[i][0])
