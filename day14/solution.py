import re
from itertools import product

with open('input') as f:
    program = list(map(lambda s: s.strip(), f.readlines()))


def apply_mask(value, current_mask):
    value = '{0:b}'.format(value)
    value = '0' * (len(current_mask) - len(value)) + value
    result = ''
    for m, v in zip(current_mask, value):
        if m == 'X':
            result += v
        else:
            result += m
    return int(result, 2)


def part_1(program):
    memory = {}
    current_mask = None
    for line in program:
        if line.startswith('mask'):
            current_mask = line.split('=')[1].strip()
        else:
            address = int(re.match(r'mem\[(\d+)].*?', line).group(1))
            value = int(re.match(r'.*=\s(\d+).*?', line).group(1))
            memory[address] = apply_mask(value, current_mask)
    print(sum(memory.values()))


part_1(program)


def apply_mask_to_address(address, current_mask):
    address = '{0:b}'.format(address)
    address = '0' * (len(current_mask) - len(address)) + address
    result = ''
    for m, v, i in zip(current_mask, address, range(len(current_mask))):
        if m == '0':
            result += v
        elif m == '1':
            result += m
        else:
            result += '{}'
    all_x = list(product('01', result.count('X')))

    return [int(result.format(*x), 2) for x in all_x]


def part_2(program):
    memory = {}
    current_mask = None
    for line in program:
        if line.startswith('mask'):
            current_mask = line.split('=')[1].strip()
        else:
            address = int(re.match(r'mem\[(\d+)].*?', line).group(1))
            value = int(re.match(r'.*=\s(\d+).*?', line).group(1))
            for a in apply_mask_to_address(address, current_mask):
                memory[a] = value
    print(sum(memory.values()))


part_2(program)
