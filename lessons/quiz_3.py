a: list[int] = [10,20,30]
b: list[int] = [30,40,50]
c: list[int] = []

for i in range(len(a)):
    c.append(a[i] + b[i])

print(c)