"""
Bags must be color-coded and must contain specific quantities of other color-coded bags.
Each line of input specifies rule for one color code.

P1. How many bag colors can eventually contain at least one shiny gold bag?

P2. How many individual bags are required inside your single shiny gold bag?
"""

import re

bag_regex = r'(\w+\s\w+) bags contain'
include_bags_regex = r'\d (\w+\s\w+)'
include_bags_regex_with_count = r'(\d \w+\s\w+)'

count = 0
colors = dict()
colors_with_count = dict()
with open('input') as f:
    for line in f:
        color = re.match(bag_regex, line.strip()).group(1)
        colors[color] = re.findall(include_bags_regex, line)
        colors_with_count[color] = re.findall(include_bags_regex_with_count, line)


def bag_contains(color):
    if not colors[color]:
        return False
    elif 'shiny gold' in colors[color]:
        return True
    else:
        for c in colors[color]:
            if bag_contains(c):
                return True


for k in colors.keys():
    count += bool(bag_contains(k))


def bags_count(color):
    count = 0
    if not colors_with_count[color]:
        return 0
    for c in colors_with_count[color]:
        i, cl = c.split(maxsplit=1)
        count += int(i) * bags_count(cl) + int(i)
    return count


print(count)
print(bags_count('shiny gold'))
