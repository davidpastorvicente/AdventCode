"""Day 4 of 2020 Advent of Code"""

import re


def del_cid(data):
    if 'cid' in data.keys():
        del data['cid']
    return data


def to_dict(data):
    it = iter(data)
    return del_cid(dict(zip(it, it)))


file = open('./input4.txt')
text = file.read()

lines = text.split('\n\n')
lines = list(map(lambda x: re.sub(r'[\n:]', ' ', x).split(), lines))
passports = list(map(to_dict, lines))

# First problem

count = 0
for i in passports:
    if len(i) == 7:
        count += 1

print(count)


# Second problem

def check_range(number, start, end):
    return start <= int(number) <= end


def check_hgt(height):
    if height.endswith('cm'):
        return check_range(height[:-2], 150, 193)
    if height.endswith('in'):
        return check_range(height[:-2], 59, 76)
    return False


def check_hcl(color):
    return re.match(r'#[0-9a-f]{6}', color) is not None


def check_ecl(color):
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_pid(number):
    return len(number) == 9 and number.isdigit()


count = 0
for i in passports:
    if len(i) == 7:
        if check_range(i['byr'], 1920, 2002) and check_range(i['iyr'], 2010, 2020) and \
                check_range(i['eyr'], 2020, 2030) and check_hgt(i['hgt']) and \
                check_hcl(i['hcl']) and check_ecl(i['ecl']) and check_pid(i['pid']):
            count += 1

print(count)
