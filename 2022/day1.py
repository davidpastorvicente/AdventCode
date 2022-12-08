file = open('inputs/input1.txt')
text = file.read()[:-1]

amounts = text.split('\n\n')
amounts = list(map(lambda x: list(map(int, x.split('\n'))), amounts))

# First part

amounts = list(map(sum, amounts))
print(max(amounts))


# Second part

amounts = list(reversed(sorted(amounts)))
print(amounts[0] + amounts[1] + amounts[2])
