"""
P1. Starting at the top-left corner of your map (input) and following a slope of right 3 and down 1, how many trees (#) would you encounter?

P2. Follow different slopes and multiply number of trees found in each one
"""

with open('input') as f:
    map_pattern = list(map(lambda s: s.strip(), f.readlines()))


def traverse(map_pattern, slope):
    right, down = slope
    i = 0
    j = 0
    trees_counter = 0
    row_length = len(map_pattern[i])

    while i < len(map_pattern):
        if map_pattern[i][j] == '#':
            trees_counter += 1
        i += down
        j += right
        j = j % row_length
    return trees_counter


result = 1

for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    result *= traverse(map_pattern, slope)

print(result)
