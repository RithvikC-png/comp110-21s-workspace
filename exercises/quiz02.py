

def sum_list(xs: list[int]) -> int:
    if len(xs) < 2:
        return xs[0]

    i: int = 1
    while i < len(xs):
        xs[i] = xs[i-1] + xs[i]
        i += 1
    
    return xs[i - 1]


def sum_ints(x0: int, x1: int, x2: int) -> int:
    x1 = x0 + x1
    x2 = x1 + x2
    return x2


points: list[int] = [1,2,3]
total: int

total = sum_ints(points[0], points [1], points [2])
print(total)


total = sum_list(points)
print(total)