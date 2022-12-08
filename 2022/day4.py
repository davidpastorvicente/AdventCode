file = open('inputs/input4.txt')
text = file.read()[:-1]

assignments = text.split('\n')


def get_ranges(assignment):
    first, second = assignment.split(',')
    first_ini, first_end = list(map(int, first.split('-')))
    second_ini, second_end = list(map(int, second.split('-')))

    return [list(range(first_ini, first_end + 1)), list(range(second_ini, second_end + 1))]


assignments = list(map(get_ranges, assignments))


# First part

def check_full_overlap(first, second):
    return all(i in first for i in second) or all(i in second for i in first)


new_assignments = list(map(lambda x: check_full_overlap(*x), assignments))
print(sum(new_assignments))


# Second part

def check_overlap(first, second):
    return any(i in first for i in second) or any(i in second for i in first)


new_assignments = list(map(lambda x: check_overlap(*x), assignments))
print(sum(new_assignments))
