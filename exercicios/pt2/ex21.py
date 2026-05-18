def potencia(base, exponente=2):
    return pow(base,exponente)

num = float(input('Digite seu número: '))
exponente = input('Digite seu exponente: ')

if exponente:
    print(f'A potência de {num} é {potencia(num,exponente)}')
else:
    print(f'A potência de {num} é {potencia(num)}')
    
