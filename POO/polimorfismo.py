class Cachorro():
    def emitirSom(self):
        print('Latir!!')

class Gato():
    def emitirSom(self):
        print('Miar!!')
        
animais = [Cachorro(), Gato()]

for animal in animais:
    animal.emitirSom()