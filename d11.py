with open("d11.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
    w, h = len(lines[0]), len(lines)

    def at(lines, x, y):
        if x >= 0 and x < w:
            if y >= 0 and y < h:
                return lines[y][x]
        return '.'

    def neigh(lines, x, y):
        return [
            at(lines, x+dx, y+dy)
            for dx in (-1, 0, 1)
            for dy in (-1, 0, 1)
            if not (dx == dy == 0)
        ]

    def show(lines):
        print()
        for line in lines:
            print(line)
        print()


def run(lines, w, h, neigh, occupied_thresh):
    step = 0
    dirty = True
    while dirty:
        dirty = False
        new_lines = []
        for y, line in enumerate(lines):
            new_line = []
            for x, c in enumerate(line):
                n = neigh(lines, x, y)
                assert len(n) == 8
                occupied = len([f for f in n if f == '#'])
                if c == 'L' and occupied == 0:
                    new_line.append('#')
                    dirty = True
                elif c == '#' and occupied >= occupied_thresh:
                    new_line.append('L')
                    dirty = True
                else:
                    new_line.append(c)
            new_lines.append("".join(new_line))
        lines = new_lines
        step += 1
        if not dirty:
            break

    print(step)
    show(lines)
    return sum([1 for line in lines for c in line if c == '#'])


print(run(lines, w, h, neigh, 4))


def first(lines, x, y, dx, dy):
    while 0 <= x < w and 0 <= y < h:
        c = at(lines, x+dx, y+dy)
        if c != '.':
            return c
        x += dx
        y += dy
    return '.'


def neigh2(lines, x, y):
    return [
        first(lines, x, y, dx, dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if not (dx == dy == 0)
    ]


print(run(lines, w, h, neigh2, 5))
