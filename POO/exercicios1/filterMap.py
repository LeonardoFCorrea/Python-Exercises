# numero = input('Digite um número: ')

# numeroFiltrado = filter(lambda x: int(x) % 2 == 0, numero)
# if numeroFiltrado:
#     numeroMapeado = map(lambda x: int(x), numeroFiltrado)
#     print('O número é par')

# print(f"Números pares: {list(numeroMapeado)}")

carros = input('Digite os nomes dos carros separados por vírgula: ')
carrosSeparados = carros.split(',')
carrosSeparados2 = map(lambda x: x.strip(), carrosSeparados)
carrosFiltrados = filter(lambda x: 'a' in x[0].lower(), carrosSeparados2)
carrosMapeados = map(lambda x: x.strip(), carrosFiltrados)

print('Carros que começam com a letra "a":')
for carro in carrosMapeados:
    print(carro)