def cubo(x):
    lambda1 = lambda x: pow(x,3)  # noqa: E731
    return lambda1(x)

print(cubo(2))

def mult(x, y):
    lambda1 = lambda x, y: x * y  # noqa: E731
    return lambda1(x,y)

print(mult(10, 2))