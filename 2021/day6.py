"""Day 6 of 2021 Advent of Code"""

file = open('inputs/input6.txt')
text = file.read()

fishes = list(map(int, text.split(',')))


# First problem

def live_day(timers):
    new = 0
    for i in range(len(timers)):
        if timers[i] > 0:
            timers[i] -= 1
        else:
            timers[i] = 6
            new += 1

    for i in range(new):
        timers.append(8)

    return timers


new_fishes = fishes.copy()
for day in range(80):
    new_fishes = live_day(new_fishes)

print(len(new_fishes))


# Second problem

def count_children(timers, days):
    children = [0] * 9
    for timer in timers:
        children[timer] += 1

    for _ in range(days):
        new_children = children.copy()
        for i in range(8):
            children[i] = new_children[i+1]
        children[6] += new_children[0]
        children[8] = new_children[0]
        print(children)

    return sum(children)


print(count_children(fishes, 256))
