

start: dict[int, list[int]] = {2: [1,2], 5: [3,4]}

def dictTRansform(xs: dict[int, list[int]]) -> dict[int, list[int]]:
    for nums in xs:
       for i in range(len(xs[nums])):
           xs[nums][i] *= nums
    
    return xs

print(start)
print(dictTRansform(start))