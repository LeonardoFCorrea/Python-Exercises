# Usando Listaa
# paises_capitais = [['Brasil', 'Brasília'], ['Japão', 'Tóquio'], ['Canadá', 'Ottawa'], ['França', 'Paris'], ['Austrália', 'Camberra']]

# pais_entrada = str(input('Digite um país: '))

# for pais, capital in paises_capitais:
#     if pais_entrada == pais:
#         print(f'A capital de {pais} é {capital}')
#         break

# Usando Dicionário
paises_capitais = {
    'Brasil': 'Brasília',
    'Japão': 'Tóquio',
    'Canadá': 'Ottawa',
    'França': 'Paris',
    'Austrália': 'Camberra',
}

pais_entrada = str(input('Digite um país: '))

if pais_entrada in paises_capitais:
    print(f'A capital do(a) {pais_entrada} é {paises_capitais[pais_entrada]}')