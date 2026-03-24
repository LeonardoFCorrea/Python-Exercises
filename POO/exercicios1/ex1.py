class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def mostrar_dados(self):
        print(f'Nome: {self.nome} \nIdade: {self.idade}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'Salário: {self.salario}')

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
        super().__init__(nome, idade, salario)
        self.departamento = departamento
        
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'Departamento: {self.departamento}')
        
pessoa = Pessoa('Leo', 12)
pessoa.mostrar_dados()

print('--------------------------------')

funcionario1 = Funcionario('Fernando', 18, 2500)
funcionario1.mostrar_dados()

print('--------------------------------')

gerente1 = Gerente('Fernando', 18, 2500, 'RH')
gerente1.mostrar_dados()