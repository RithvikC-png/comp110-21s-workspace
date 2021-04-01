

start: dict[int, list[int]] = {2: [1,2], 5: [3,4]}

def dictTRansform(xs: dict[int, list[int]]) -> dict[int, list[int]]:
    for nums in xs:
        N: list[int] = xs[nums]
        L: int = len(N)
        i: int = 0
        while i < L:
            xs[nums] = nums * N
    
    return xs

print(start)
print(dictTRansform(start))