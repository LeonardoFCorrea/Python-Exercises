class Pessoa():
    def __init__(self, nome):
        self.nome = nome

class Nadador(Pessoa):
    def nadar(self):
        print(f'O {self.nome} está nadando!')

class Corredor(Pessoa):
    def correr(self):
        print(f'O {self.nome} está correndo!')
        
class Triatleta(Nadador, Corredor):
    def competir(self):
        self.nadar()
        self.correr()
        
nadador1 = Nadador('Roberto')
nadador1.nadar()

corredor1 = Corredor('Ricardo')
corredor1.correr()

triatleta1 = Triatleta('Usain Bolt')
triatleta1.competir()