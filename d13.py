import functools


def parse(s):
    try:
        return int(s)
    except ValueError:
        return 0


with open("d13.txt", "r") as f:
    lines = f.readlines()
    ts = int(lines[0])
    in_service = [parse(w) for w in lines[1].split(',')]


min, min_id = max(in_service), 0
for i in in_service:
    if not i:
        continue

    d = int(ts / float(i))
    if d * i == ts:
        min, min_id = 0, i
        break

    if min > (d + 1) * i - ts:
        min, min_id = (d + 1) * i - ts, i
        continue

print(min * min_id)


def euc(a, b):
    aO, bO = a, b

    x = lasty = 0
    y = lastx = 1
    while b != 0:
        q = int(a / b)
        a, b = b, a % b
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y

    return (lastx, lasty, aO * lastx + bO * lasty)


def solve(rests, modulos):
    x = 0
    M = functools.reduce(lambda x, y: x * y, modulos)

    for mi, resti in zip(modulos, rests):
        Mi = int(M / mi)
        s = euc(Mi, mi)[0]
        e = s * Mi
        x += resti * e
    return M - ((x % M) + M) % M


cs = [i for i, v in enumerate(in_service) if v != 0]
mods = [v for v in in_service if v != 0]
print(solve(cs, mods))
