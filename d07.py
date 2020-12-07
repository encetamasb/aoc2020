import re


with open("d07.txt2", "r") as f:
    nodes = {}
    for line in f.readlines():
        node = list(re.findall(r'^(\w+ \w+) bags contain', line))[0]
        children = {
            s: int(i)
            for (i, s) in list(re.findall(r'(\d+) (\w+ \w+) bag', line))
        }
        nodes[node] = children

    names = {'shiny gold', }
    dirty = True
    while dirty:
        cur = len(names)
        for name, ch in nodes.items():
            names |= {
                name
                for n in names
                if n in ch
            }
        dirty = cur != len(names)
    print(len(names) - 1)

    def calc2(n):
        c = 1
        for chn, chm in nodes[n].items():
            c += chm * calc2(chn)
        return c

    print(calc2('shiny gold') - 1)
