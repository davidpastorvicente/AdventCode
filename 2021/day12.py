"""Day 12 of 2021 Advent of Code"""

file = open('inputs/input12.txt')
text = file.read()

directions = list(map(lambda x: x.split('-'), text.split('\n')))
connections = {}

for dr in directions:
    if dr[0] in connections:
        connections[dr[0]].append(dr[1])
    else:
        connections[dr[0]] = [dr[1]]

for cn in connections.copy():
    for dest in connections[cn]:
        if dest not in connections:
            connections[dest] = [cn]
        elif cn not in connections[dest]:
            connections[dest].append(cn)


# First problem

def get_paths_v1(ini, end, visited, count):
    if ini.islower():
        visited[ini] = True

    if ini == end:
        count[0] += 1
    else:
        for i in connections[ini]:
            if not visited[i]:
                get_paths_v1(i, end, visited, count)

    visited[ini] = False


def count_paths_v1(ini, end):
    visited, count = {i: False for i in connections}, [0]
    get_paths_v1(ini, end, visited, count)

    return count[0]


print(count_paths_v1('start', 'end'))


# Second problem

def get_paths_v2(ini, end, visited, count, cave, rep):
    if ini.islower():
        if ini != cave or rep[0]:
            visited[ini] = True
        else:
            rep[0] = True

    if ini == end:
        count[0] += 1
    else:
        for i in connections[ini]:
            if not visited[i]:
                get_paths_v2(i, end, visited, count, cave, rep)

    visited[ini] = False


def count_paths_v2(ini, end):
    small_caves = [i for i in connections if i.islower() and i != 'start' and i != 'end']

    total = 0
    for cave in small_caves:
        visited, count = {i: False for i in connections}, [0]
        get_paths_v2(ini, end, visited, count, cave, [False])
        total += count[0]

    return total


print(count_paths_v2('start', 'end'))
