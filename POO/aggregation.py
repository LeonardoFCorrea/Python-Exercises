class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []
    
    def adicionarMotor(self, motor):
        self.motores.append(motor)
        
    def listarMotores(self):
        for motor in self.motores:
            print(f'Marca: {motor.marca} - {motor.potencia} cavalos de potência')
        
motorV6 = Motor('Ford', 300)
motorV8 = Motor('Ferrari', 650)
motorV12 = Motor('Lamborghini', 950)

carro1 = Carro()
carro1.adicionarMotor(motorV6)
carro1.adicionarMotor(motorV8)
carro1.adicionarMotor(motorV12)

carro1.listarMotores()