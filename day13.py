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
