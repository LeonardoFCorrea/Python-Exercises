def desconto(valor, porcentagem):
    return valor - (valor * porcentagem / 100)

def media(*args):
    return sum(args) / len(args) 