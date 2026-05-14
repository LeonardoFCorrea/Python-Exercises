from modulosFolder.funcoes import somar, multi

resultado = somar(5, 3)
resultado_multi = multi(5, 3)
print(f"O resultado da soma é: {resultado} \nE da multiplicação é: {resultado_multi}")

numeros = set()
numeros.add(resultado)
numeros.add(resultado_multi)
print(numeros)

