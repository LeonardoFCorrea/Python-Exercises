numerosPares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9]

numerosParesFiltrados = filter(lambda x: x < 4, numerosPares)
print(list(numerosParesFiltrados))  # Imprime os números pares menores que 4

def multiplicar(x):
    lambda1 = lambda x: x * 2  # noqa: E731
    return lambda1(x) * 2

print(multiplicar(5))  # Imprime o resultado da função multiplicar com o valor 5