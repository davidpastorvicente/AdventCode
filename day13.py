"""Day 13 of 2020 Advent of Code"""

file = open('./input13.txt')
text = file.read()

lines = text.split('\n')


# First problem

timestamp = int(lines[0])
buses = [int(i) for i in lines[1].split(',') if i.isdigit()]

best, bus = (timestamp//buses[0] + 1) * buses[0] - timestamp, buses[0]
for i in range(1, len(buses)):
    time = (timestamp//buses[i] + 1) * buses[i] - timestamp
    if time < best:
        best = time
        bus = buses[i]

print(best * bus)


# Second problem

buses = [[int(bus), i] for i, bus in enumerate(lines[1].split(',')) if bus.isdigit()]

num, found = -1, False
while not found:
    print(num)
    num += 1
    for i in buses:
        if (num + i[1]) % i[0] == 0:
            found = True
        else:
            found = False
            break

print(num)
