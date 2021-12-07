"""Day 7 of 2021 Advent of Code"""

file = open('inputs/input7.txt')
text = file.read()

crabs = list(map(int, text.split(',')))


# First problem

def get_fuel_v1(positions, num):
    return sum([abs(num-i) for i in positions])


min_fuel = get_fuel_v1(crabs, 0)
for pos in range(1, max(crabs)):
    min_fuel = min(min_fuel, get_fuel_v1(crabs, pos))

print(min_fuel)


# Second problem

def get_fuel_v2(positions, num):
    return sum([abs(num-i) * (abs(num-i)+1)//2 for i in positions])


min_fuel = get_fuel_v2(crabs, 0)
for pos in range(1, max(crabs)):
    min_fuel = min(min_fuel, get_fuel_v2(crabs, pos))

print(min_fuel)
