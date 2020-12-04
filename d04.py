import re

keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')

with open("d04.txt", "r") as f:
    data = []
    d = {}
    for line in f.readlines():
        if not line.strip():
            if d:
                data.append(d)
                d = {}
            continue
        items = list(re.findall(r'(\w+):(\S+)', line))
        for k, v in items:
            if k in keys:
                d[k] = v
    if d:
        data.append(d)

ret0 = 0
for d in data:
    diff = set(keys) - set(d.keys())
    if not diff or (len(diff) == 1 and 'cid' in diff):
        ret0 += 1

print(ret0)


ret1 = 0
for d in data:
    diff = set(keys) - set(d.keys())
    if not diff or (len(diff) == 1 and 'cid' in diff):
        try:
            assert 2002 >= int(d['byr']) >= 1920
            assert 2020 >= int(d['iyr']) >= 2010
            assert 2030 >= int(d['eyr']) >= 2020
            hgt = re.match(r'^(\d+)(cm|in)$', d['hgt'])
            assert hgt
            hgt_v, hgt_m = int(hgt.groups()[0]), hgt.groups()[1]
            assert (
                (hgt_m == 'in' and 76 >= hgt_v >= 59) or
                (hgt_m == 'cm' and 193 >= hgt_v >= 150)
            )
            assert re.match(r'^#[0-9a-f]{6}$', d['hcl'])
            assert d['ecl'] in ('amb', 'blu', 'brn',
                                'gry', 'grn', 'hzl', 'oth')

            assert re.match(r'^\d{9}$', d['pid'])
        except (AssertionError, ValueError):
            continue

        ret1 += 1

print(ret1)
