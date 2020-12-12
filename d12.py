from collections import namedtuple

with open("d12.txt", "r") as f:
    moves = [line for line in f.readlines()]

Vec = namedtuple('Vec', ['x', 'y'])


def add(v: Vec, w: Vec) -> Vec:
    return Vec(v[0] + w[0], v[1] + w[1])


def rot90(v: Vec) -> Vec:
    return Vec(v[1], -v[0])


def mul(v: Vec, m: int) -> Vec:
    return Vec(v[0] * m, v[1] * m)


def run1(state, m):
    d, v = m[0], int(m[1:])

    if d == 'F':
        return (add(state[0], mul(state[1], v)), state[1])
    if d == 'N':
        return (add(state[0], Vec(0, v)), state[1])
    if d == 'S':
        return (add(state[0], Vec(0, -v)), state[1])
    if d == 'W':
        return (add(state[0], Vec(-v, 0)), state[1])
    if d == 'E':
        return (add(state[0], Vec(v, 0)), state[1])
    if d == 'R':
        heading = state[1]
        for i in range(int(v / 90)):
            heading = rot90(heading)
        return (state[0], heading)
    if d == 'L':
        heading = state[1]
        for i in range(int((360 - v) / 90)):
            heading = rot90(heading)
        return (state[0], heading)


state = (Vec(0, 0), Vec(1, 0))

for m in moves:
    state = run1(state, m)

print(abs(state[0][0]) + abs(state[0][1]))


def run2(state, m):
    d, v = m[0], int(m[1:])

    if d == 'F':
        return (state[0], add(state[1], mul(state[0], v)))
    if d == 'N':
        return (add(state[0], Vec(0, v)), state[1])
    if d == 'S':
        return (add(state[0], Vec(0, -v)), state[1])
    if d == 'W':
        return (add(state[0], Vec(-v, 0)), state[1])
    if d == 'E':
        return (add(state[0], Vec(v, 0)), state[1])
    if d == 'R':
        heading = state[0]
        for i in range(int(v / 90)):
            heading = rot90(heading)
        return (heading, state[1])
    if d == 'L':
        heading = state[0]
        for i in range(int((360 - v) / 90)):
            heading = rot90(heading)
        return (heading, state[1])


state = (Vec(10, 1), Vec(0, 0))

for m in moves:
    state = run2(state, m)

print(abs(state[1][0]) + abs(state[1][1]))
