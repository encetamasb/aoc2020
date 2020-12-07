
def parse(s: str, bounds):
    if not s:
        return bounds[0]
    if s[0] in ('F', 'L'):
        return parse(
            s[1:], (bounds[0], bounds[0] + (bounds[1] - bounds[0]) / 2))
    return parse(
        s[1:], (bounds[0] + (bounds[1] - bounds[0]) / 2, bounds[1]))


with open("d05.txt", "r") as f:
    data = [
        (
            parse(line.strip()[:7], (0, 128)),
            parse(line.strip()[7:], (0, 8))
        )
        for line in f.readlines()
    ]

    ids = [
        row[0] * 8 + row[1]
        for row in data
    ]

    print(max(ids))

    ids.sort()

    print([id for i, id in enumerate(ids[:-2]) if ids[i+1] == id + 2][0] + 1)
