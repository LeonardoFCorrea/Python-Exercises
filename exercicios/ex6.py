frutas = ['maçã', 'banana', 'manga', 'uva']

print(frutas)

print(f'A primeira fruta é a {frutas[0]} e última é a {frutas[-1]}')

frutas[1] = 'morango'
frutas.append('abacaxi')
print(frutas)

frutas.remove('manga')
del(frutas[-1],)
print(frutas)

for fruta in frutas:
    print(f'{fruta}', end=', ')