idade = int(input('Digite sua idade: '))

if idade < 13:
    print('Você é uma criança.')
elif idade in range(13,20):
    print('Você é um adolescente')
elif idade >= 20:
    print('Você é um adulto')