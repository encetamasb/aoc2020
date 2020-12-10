with open("d09.txt", "r") as f:
    nums = [
        int(line.strip())
        for line in f.readlines()
        if line.strip()
    ]


def calc1(plen, nums):
    cur = plen
    preamble = nums[:cur]
    psets = [
        {n+m for j, m in enumerate(preamble) if n != m}
        for i, n in enumerate(preamble)
    ]

    while cur < len(nums):
        v = nums[cur]
        if not any(map(lambda s: v in s, psets)):
            return v

        preamble = preamble[1:]
        preamble.append(v)

        psets = psets[1:]
        psets.append({v+n for n in preamble if v != n})

        cur += 1

    return None


v = calc1(25, nums)
print(v)


def calc2(v, nums):
    b, e = 0, 1
    tot = sum(nums[b:e+1])
    while tot != v:
        if tot > v:
            b += 1
        else:
            e += 1
        tot = sum(nums[b:e+1])
    return min(nums[b:e+1]) + max(nums[b:e+1])


print(calc2(v, nums))
