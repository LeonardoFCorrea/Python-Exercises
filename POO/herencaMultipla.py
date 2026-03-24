class Animal():
    def __init__(self,nome):
        self.nome = nome

class Predador(Animal):
    def cacando(self):
        print(f'O {self.nome} está caçando!')

class Presa(Animal):
    def fugindo(self):
        print(f'O {self.nome} está sendo caçado!')

class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass

coelho1 = Coelho('Coelhin')
tigre1 = Tigre('Bang')
golfinho1 = Golfinho('Buggy')

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()