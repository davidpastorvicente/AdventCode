"""Day 4 of 2021 Advent of Code"""

import numpy as np

file = open('inputs/input4.txt')
text = file.read()

parts = text.split('\n\n')
numbers = list(map(int, parts[0].split(',')))
boards = list(map(lambda x: np.array(list(map(lambda y: list(map(int, y.split())), x.split('\n')))), parts[1:]))


# First problem

def is_winner(board):
    for i in range(len(board)):
        if np.all(board[i] == -1):
            return True

    for i in range(len(board[0])):
        if np.all(board[:, i] == -1):
            return True

    return False


def play_bingo_v1(nums, brds):
    for num in nums:
        for i in range(len(brds)):
            brds[i] = np.where(brds[i] == num, -1, brds[i])
            if is_winner(brds[i]):
                return num, brds[i]


number, winner = play_bingo_v1(numbers, boards.copy())
print(number * sum(i for i in winner.flatten() if i != -1))


# Second problem

def play_bingo_v2(nums, brds):
    players = list(range(len(brds)))
    for num in nums:
        for i in range(len(brds)):
            brds[i] = np.where(brds[i] == num, -1, brds[i])
            if is_winner(brds[i]) and i in players:
                if len(players) > 1:
                    players.remove(i)
                else:
                    return num, brds[i]


number, winner = play_bingo_v2(numbers, boards.copy())
print(number * sum(i for i in winner.flatten() if i != -1))
