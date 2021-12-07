"""Day 15 of 2020 Advent of Code"""

file = open('inputs/input15.txt')
text = file.read()

numbers = list(map(int, text.split(',')))


def ini_hist():
    hist = {}
    for i in range(len(numbers)):
        hist[numbers[i]] = [i + 1]

    return hist


def add_turn(n, n_turn, hist):
    if n not in hist.keys():
        hist[n] = []
    elif len(hist[n]) > 1:
        hist[n].pop(0)
    hist[n].append(n_turn)


def play_game(turns):
    turn, last, new = len(numbers), numbers[-1], 0
    hist = ini_hist()
    while turn < turns:
        turn += 1
        new = 0 if len(hist[last]) < 2 else hist[last][1] - hist[last][0]

        add_turn(new, turn, hist)
        last = new

    return new


# First problem

print(play_game(2020))


# Second problem

print(play_game(30000000))
