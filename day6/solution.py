"""
Input constits of groups separated by newline.
Each line represents question numbers (letters a - z) group member answered "yes".

P1. For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

P2. For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""

with open('input') as f:
    data = f.readlines()


def count_anyone(data):
    group = ''
    count = 0
    for line in data:
        if line == '\n':
            count += len(set(group))
            group = ''
        else:
            group += line.strip()
    return count


print(count_anyone(data))


def count_everyone(data):
    first_line = True
    count = 0
    group = None
    for line in data:
        if line == '\n':
            count += len(group)
            first_line = True
        else:
            group = set(line.strip()) if first_line else group.intersection(set(line.strip()))
            first_line = False
    return count


print(count_everyone(data))
