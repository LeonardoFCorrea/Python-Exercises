def calculadora(operacaoMath):
    def wrapper(*args, **kwargs):
        print('Calculando os Números...')
        operacaoMath(*args)
    
    return wrapper


@calculadora
def soma(n1, n2):
    res = n1 + n2
    print(res)
    
soma(10, 10)


        
    