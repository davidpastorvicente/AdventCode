file = open('inputs/input2.txt')
text = file.read()[:-1]

CHANGE = {'A': 'X', 'B': 'Y', 'C': 'Z'}
POINTS = {'X': 1, 'Y': 2, 'Z': 3}

plays = text.split('\n')
plays = list(map(lambda x: [CHANGE.get(x.split()[0]), x.split()[1]], plays))


# First part

def get_points(*args):
    a, b = args[0]
    if a == b:
        return 3 + POINTS[b]
    if (chr(ord(a) + 1) == b and a != 'Z') or (a == 'Z' and b == 'X'):
        return 6 + POINTS[b]
    return POINTS[b]


points = list(map(get_points, plays))
print(sum(points))


# Second part


def get_points_v2(*args):
    a, b = args[0]
    if b == 'Y':
        return 3 + POINTS[a]
    if b == 'X':
        return POINTS[chr(ord(a) - 1) if a != 'X' else 'Z']
    return 6 + POINTS[chr(ord(a) + 1) if a != 'Z' else 'X']


points = list(map(get_points_v2, plays))
print(sum(points))
