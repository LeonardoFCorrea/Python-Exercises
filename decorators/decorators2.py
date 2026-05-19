def calculadora(operacao):
    def wrapper(*args):
        print('Selecionando operação matemática...')
        operacao(*args)
    return wrapper
        

@calculadora
def soma(n1, n2):
    sum = n1 + n2
    print(sum)

@calculadora
def subtracao(n1, n2):
    return n1 - n2

soma(10, 12)