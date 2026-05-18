carros_estoque = ['BMW X6', 'BMW i5', 'BMW i8']

carro = str(input('Digite qual carro você deseja comprar: (veremos se está disponível)'))

if carro in carros_estoque:
    print(f'O {carro} está em estoque Sr(Sra)')
else:
    print(f'O {carro} não está disponível Sr(Sra)')