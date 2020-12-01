"""
    P1. Find two numbers in array which sum is given number (2020)
    P2. Do the same for three numbers
"""
with open('input') as f:
    numbers = sorted(list(map(int, f.readlines())))


def find_sum(array, target=2020):
    i = 0
    j = len(array) - 1
    while i < j:
        s = array[i] + array[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
            j = len(array) - 1
        else:
            return array[i], array[j]
    return None


for idx in range(len(numbers)):
    result = find_sum(numbers[idx + 1:], 2020 - numbers[idx])
    if result is not None:
        print(numbers[idx], *result)
        print(result[0] * result[1] * numbers[idx])
        break
