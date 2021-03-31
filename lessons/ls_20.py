def add(xs: list[int]) -> int:
    if len(xs) == 0:
        return 0
    else:
        x: int = xs.pop()
        y = add(xs)
        return (x + y)



nums: list[int] = [1, 2, 3]
print(add(nums))
print(len(nums))