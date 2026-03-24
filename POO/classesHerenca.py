class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie
        
    def informar(self):
        print(f'Eu sou o {self.especie} chamado {self.nome}')
        
class Gato(Animal):
    def emitirSom(self):
        print(f'Miau!')
        
    def arranhar(self):
        print(f'O gato {self.nome} está arranhando')

class Cachorro(Animal):
    def emitirSom(self):
        print(f'Au Au!')

class Elefante(Animal):
    def emitirSom(self):
        print(f'Fuuuuu')

gato1 = Gato('Felix', 'Preto', 'felino')
gato1.informar()
gato1.emitirSom()
gato1.arranhar()

print('---------------------')

cachorro1 = Cachorro('Pluto', 'Marrom', 'Pastor Inglês')
cachorro1.informar()
cachorro1.emitirSom()

print('---------------------')

elefante1 = Elefante('Ricardo', 'Marrom', 'Elefante Africano')
elefante1.informar()
elefante1.emitirSom()

print('---------------------')