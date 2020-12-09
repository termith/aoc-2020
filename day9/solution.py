from day1.solution import find_sum

with open('input') as f:
    data = list(map(int, f.readlines()))

idx = 25
wrong_number = None
while idx < len(data):
    if find_sum(sorted(data[idx - 25:idx]), target=data[idx]) is None:
        wrong_number = data[idx]
        print(f'Wrong number is {wrong_number}')
        break
    idx += 1

i = 0
j = 1

while True:
    result = data[i]
    while result < wrong_number:
        result += data[j]
        j += 1
    if result == wrong_number:
        break
    else:
        i += 1
        j = i + 1
print(max(data[i:j]) + min(data[i:j]))
