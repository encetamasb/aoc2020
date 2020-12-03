import re

with open("d02.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

rows = []
for line in lines:
    parts = list(re.findall(r'(\d+)-(\d+) (\w): (\w+)', line))[0]
    rows.append((int(parts[0]), int(parts[1]), parts[2], parts[3]))

ret0 = 0
for row in rows:
    if row[1] >= row[3].count(row[2]) >= row[0]:
        ret0 += 1
        print(row[3].count(row[2]), row)


print(ret0)

ret1 = 0
for row in rows:
    a, b = row[3][row[0] - 1], row[3][row[1] - 1]
    if a != b and (a == row[2] or b == row[2]):
        ret1 += 1

print(ret1)
