class Animal():
    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f'O {self.nome} está comendo!')

class Mamifero(Animal):
    def andar(self):
        print(f'O mamífero {self.nome} está andando!')

class Ave(Animal):
    def voar(self):
        print(f'A ave {self.nome} está voando!')
        
class Morcego(Mamifero, Ave):
    def acao(self):
        self.comer()
        self.andar()
        self.voar()
        
morcego1 = Morcego('Morceguin')
morcego1.acao()