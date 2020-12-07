with open("d06.txt", "r") as f:
    groups = [set(g.strip().replace("\n", "")) for g in f.read().split("\n\n")]
    print(sum(list(map(len, groups))))


def allyes(sets):
    ret = sets[0]
    for s in sets[1:]:
        ret &= s
    return ret


with open("d06.txt", "r") as f:
    groups2 = [
        allyes([set(line) for line in g.strip().split()])
        for g in f.read().split("\n\n")
    ]
    print(sum(list(map(len, groups2))))
