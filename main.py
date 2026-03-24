import funcoes

valor = float(input('Digite seu valor em Real a ser descontado: '))

print(f'O Valor descontado fica R${funcoes.desconto(valor, 10):.2f}')

notas = []


while True:
    nota = input('Digite sua nota aqui (5 para parar): ')

    if nota.lower() == 'fechar':
        break

    notas.append(float(nota))

print(f'A média das suas notas ficaram: {funcoes.media(*notas):.1f}')