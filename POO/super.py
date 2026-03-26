class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status    
        
    def apresentar(self):
        print(f'Meu nome é {self.nome}')
        
    def verificarStatus(self):
        print(f'Status: {'ATIVO' if self.status else 'INATIVO'}')
        
class Aluno(Escola):
    def __init__(self, nome, idade, status, ano,):
        super().__init__(nome, idade, status)
        self.ano = ano

    def apresentar(self):
        super().apresentar()
        print(f'Tenho {self.idade} anos de idade')
    
class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia
    
    def apresentar(self):
        super().apresentar()
        print(f'Tenho {self.idade} anos de idade e sou um professor')

class Assistente(Escola):
    def __init__(self, nome, idade, status,  bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco
    
    def apresentar(self):
        super().apresentar()
        print(f'Tenho {self.idade} anos de idade e sou um assistente')

aluno1 = Aluno(nome='Leonardo', idade=13, status=True, ano=5)
print(aluno1.ano)
aluno1.apresentar()
aluno1.verificarStatus()

print('------------------------')

professor1 = Professor(nome='Newton', idade=32, status=False, materia='Física')
professor1.apresentar()
professor1.verificarStatus()