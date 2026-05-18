def elev_quadrado(x):
    lambda1 = lambda x: pow(x, 2)  # noqa: E731
    return print(f'R: {lambda1(x)}')

numeros = [1, 2, 3, 4, 5]

for num in numeros:
    elev_quadrado(num)