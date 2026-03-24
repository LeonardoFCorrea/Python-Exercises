class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f'Oiii, O meu nome é {self.nome} e tenho {self.idade} anos de idade')
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
    
    def trabalhar(self):
        print(f'{self.nome} está no meio do trabalho no cargo de {self.cargo}')
        
class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo
    
    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'A sua de compra no valor de R${valor_compra} foi confirmada! Seu saldo agora é de R${self.saldo}')                  
        else:
            print(f'Saldo insuficiente')
            
f1 = Funcionario('Ana', 42, 'RH')
f1.apresentar()
# f1.trabalhar()

print('-------------')

c1 = Cliente('Leandro', 14, 120)
# c1.apresentar()
c1.comprar(1130)