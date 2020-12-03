with open("d03.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def count(lines, dx, dy):
    x = 0
    y = 0
    cnt = 0
    while y < len(lines):
        if lines[y][x] == '#':
            cnt += 1
        x = (x + dx) % len(lines[0])
        y += dy
    return cnt


print(count(lines, 3, 1))

print(
    count(lines, 1, 1) *
    count(lines, 3, 1) *
    count(lines, 5, 1) *
    count(lines, 7, 1) *
    count(lines, 1, 2)
)
