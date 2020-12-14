from timeit import timeit
from functools import reduce

with open('input') as f:
    ts = int(f.readline())
    buses = f.readline().split(',')


def part_1(data):
    buses = list(map(int, filter(lambda x: x != 'x', data)))
    min_value = ts
    bus = 0
    for b in buses:
        if (x := b - (ts % b)) < min_value:
            min_value = x
            bus = b
    print(bus, min_value)
    print(bus * min_value)


part_1(buses)


def part_2(data):
    buses = {}
    for i, el in enumerate(data):
        if el == 'x':
            continue
        buses[int(el)] = i

    ts, step = 0, 1
    for bus, offset in buses.items():
        # Ищем ts, который делится на bus с нужным остатком
        while (ts + offset) % bus:
            ts += step
        # Мы можем увеличивать шаг, на число, делящееся на произведение всех предыдущих
        # в этом случае, мы всегда будем получать нужные остатки, так как уже нашли их на предыдущих этапах
        step *= bus

    print(ts)


part_2(buses)
