"""
Code is represented as a text file with one instruction per line of text.
Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
    * acc increases or decreases a single global value called the accumulator by the value given in the argument.
      For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0.
      After an acc instruction, the instruction immediately below it is executed next.
    * jmp jumps to a new instruction relative to itself.
      The next instruction to execute is found using the argument as an offset from the jmp instruction;
    * nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

P1. Immediately before any instruction is executed a second time, what value is in the accumulator?

P2. Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
    What is the value of the accumulator after the program terminates?
"""

from copy import copy

with open('input') as f:
    code = list(map(lambda s: s.strip(), f.readlines()))


def detect_loop(code):
    idx = 0
    acc = 0

    while idx != len(code):
        if code_copy[idx] is None:
            return acc, True
        command, number = code_copy[idx].split()
        number = int(number)
        code_copy[idx] = None
        if command == 'nop':
            idx += 1
        elif command == 'acc':
            acc += number
            idx += 1
        elif command == 'jmp':
            idx += number
    return acc, False


code_copy = copy(code)
print(detect_loop(code_copy)[0])

NOPS = []
JMPS = []

for i in range(len(code)):
    if code[i].startswith('jmp'):
        JMPS.append(i)
    elif code[i].startswith('nop'):
        NOPS.append(i)

for jmp in JMPS:
    code_copy = copy(code)
    code_copy[jmp] = code_copy[jmp].replace('jmp', 'nop')
    acc, is_loop = detect_loop(code_copy)
    if not is_loop:
        print(f'Index to change: {jmp}, acc is {acc}')
        exit(0)

for nop in NOPS:
    code_copy = copy(code)
    code_copy[nop] = code_copy[nop].replace('nop', 'jmp')
    acc, is_loop = detect_loop(code_copy)
    if not is_loop:
        print(f'Index to change: {nop}, acc is {acc}')
        exit(0)
