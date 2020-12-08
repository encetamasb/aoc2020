import re


def parse(s):
    v = int(s[1:])
    if s[0] == '-':
        v *= (-1)
    return v


def run(prog, cur, acc):
    hist = set()
    while True:
        if cur in hist:
            return (False, cur, acc)

        if cur >= len(prog):
            return (True, cur, acc)

        hist.add(cur)

        if prog[cur][0] == 'acc':
            acc += prog[cur][1]
            cur += 1
        elif prog[cur][0] == 'jmp':
            cur += prog[cur][1]
        else:
            cur += 1


with open("d08.txt", "r") as f:
    prog = [
        (g[0], parse(g[1]))
        for line in f.readlines()
        for g in re.findall(r'(\w+) ([+-]\d+)', line)
    ]

    print(run(prog, 0, 0)[2])

    for i, instr in enumerate(prog):
        if instr[0] == 'nop':
            new_prog = prog[:]
            new_prog[i] = ('jmp', instr[1])
            ret = run(new_prog, 0, 0)
            if ret[0] is True:
                break
        if instr[0] == 'jmp':
            new_prog = prog[:]
            new_prog[i] = ('nop', instr[1])
            ret = run(new_prog, 0, 0)
            if ret[0] is True:
                break
    print(ret[2])
