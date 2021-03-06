from collections import defaultdict

with open("d10.txt", "r") as f:
    jolts = [int(line) for line in f.readlines()]

jolts.append(0)
jolts.append(max(jolts) + 3)
jolts.sort()

diffs = defaultdict(lambda: 0)
for i in range(len(jolts)-1):
    diff = jolts[i+1] - jolts[i]
    diffs[diff] += 1

print(diffs[1] * diffs[3])


def brute(jolts):
    c = 1
    nxt = 1
    while nxt < len(jolts) and jolts[nxt] - jolts[0] <= 3:
        c += brute(jolts[nxt:])
        nxt += 1
    return c


threes = [i+1 for i in range(len(jolts)-1)
          if jolts[i+1] - jolts[i] == 3 and i != 0]
threes.append(0)
threes.sort()
pairs = [(a, b) for a, b in zip(threes, threes[1:])]

c = 1
for (a, b) in pairs:
    routes = max(int(brute(jolts[a:b]) / 2), 1)
    c *= routes

print(c)


# better variant for second part

d = defaultdict(lambda: 0)
d[0] = 1
for i in range(0, len(jolts)):
    v = jolts[i]
    for j in range(3):
        if i + j + 1 >= len(jolts):
            break
        w = jolts[i + 1 + j]
        if w - v <= 3:
            d[i + 1 + j] += d[i]
print(d[len(jolts)-1])


# even better variant (O(1) storage) for second part

s = [0, 1, 0, 0, 0]
for i in range(0, len(jolts)):
    s.pop(0)
    v = jolts[i]
    for j in range(3):
        if i + j + 1 >= len(jolts):
            break
        w = jolts[i + 1 + j]
        if w - v <= 3:
            s[j + 1] += s[0]
    s.append(0)
print(s[0])
