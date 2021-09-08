def f(x: float) -> int:
    return int(x)

def g(x: str) -> float:
    return float(x)

y = f(g("3.14"))

print(type(y))