def par_ou_impar(x):
    lambda1 = lambda x: 'Par' if x % 2 == 0 else 'Ímpar'  # noqa: E731
    return lambda1(x)

print(par_ou_impar(11))