numbers = [0, 3, 6]


def rfind(l, i):
    if i not in l[:-1]:
        return -1
    for idx, e in enumerate(reversed(l[:-1])):
        if e == i:
            return len(l) - idx


def part_1(start):
    turn = len(start) + 1
    while turn < 2021:
        previous = start[-1]
        i = rfind(start, previous)
        if i != -1:
            start.append(turn - i)
        else:
            start.append(0)
        turn += 1
    print(start[-1])


def part_2(numbers, stop=2020):
    turns = {n: i for i, n in enumerate(numbers)}
    current = 0
    previous = 0
    for turn in range(len(numbers), stop):
        # Сохраняем число с предыдущего хода
        previous = current
        # Если такого числа не было - 0, если было, то разница между последним ходом и текуущим
        current = 0 if current not in turns else turn - turns[current]
        # Обновляем значение для предыдущего хода
        turns[previous] = turn
    print(previous)


part_1([0, 13, 1, 16, 6, 17])
part_2([0, 13, 1, 16, 6, 17], stop=30000000)
