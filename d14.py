import re
import math

with open("d14.txt", "r") as f:
    lines = f.readlines()


def to_bin(v):
    return bin(v)[2:].zfill(36)


def maskbit(m, b):
    if m == 'X':
        return b
    return m


def masked(mask, v):
    a = to_bin(v)
    r = "".join([maskbit(m, b) for m, b in zip(mask, a)])
    return int(r, 2)


mem = {}
mask = 'X' * 36
for line in lines:
    if line.startswith('mask'):
        mask = line[7:].strip()
        continue

    addr, v = list(map(int, re.findall(r'(\d+)', line)))
    mem[addr] = masked(mask, v)

print(sum(mem.values()))


def maskbit2(m, b):
    if m == 'X':
        return 'X'
    if m == '0':
        return b
    return '1'


def masked2(mask, v):
    a = to_bin(v)
    r = "".join([maskbit2(m, b) for m, b in zip(mask, a)])
    return r


mask = 'X' * 36
addrs = {}
for line in lines:
    if line.startswith('mask'):
        mask = line[7:].strip()
        continue

    addr, v = list(map(int, re.findall(r'(\d+)', line)))
    maddr = masked2(mask, addr)
    addrs[maddr] = v


def count(s):
    return int(math.pow(2, s.count('X')))


def calc(n, group, i, last=''):
    if len(group) == 0:
        return 0

    if len(group) == 1:
        c = count(last + group[0][0][i:]) * group[0][1]
        return c

    if i == n:
        c = count(last + group[-1][0][i:]) * group[-1][1]
        return c

    g0 = [g for g in group if g[0][i] in '0X']
    g1 = [g for g in group if g[0][i] in '1X']
    return calc(n, g0, i+1, last+'0') + calc(n, g1, i+1, last+'1')


print(calc(36, [(k, v) for k, v in addrs.items()], 0))
