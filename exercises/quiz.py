a: str = "a"
b: str = "b" + a + "b"
c: str = "c" + b + "c"
n: int = len(c)

print(c[n-1])
