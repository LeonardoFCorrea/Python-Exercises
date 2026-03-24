class Veiculo():
    def __init__(self):
        pass
    
    def mover(self):
        print('Veículo em movimento')
        
class Carro(Veiculo):
    def mover(self):
        super().mover()
        print('Carro em movimento')    
        
class CarroEletrico(Carro):

    def mover(self):
        print('Carro elétrico em movimento')
    
carro = Carro()
carro.mover()

carroE = CarroEletrico()
carroE.mover()
    