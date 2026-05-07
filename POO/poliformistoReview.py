class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass
    
    def apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos de idade')
        pass
    
class Desenvolvedor(Pessoa):
    def __init__(self, nome, idade, linguagem):
        super().__init__(nome, idade)
        self.linguagem = linguagem
        pass
    
    def apresentar(self):
        super().apresentar()
        print(f'Sou um desenvolvedor de {self.linguagem}')
        pass

desenvolvedor1 = Desenvolvedor(nome='Leonardo', idade=13, linguagem='Python')
desenvolvedor1.apresentar()