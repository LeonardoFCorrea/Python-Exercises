class Carros:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.ligado = False
        self.seta = None
        
    def informacoes(self):
        print(f'A cor do carro é {self.cor}')
        print(f'A ano do carro é {self.ano}')
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro foi ligado')
        else:
            print('O carro já estava ligado')
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro já estava desligado')
    
    def ligarSeta(self, direcao):
        if not self.ligado:
            print('Ligue o carro primeiro')
            return
        
        self.seta = direcao
        print(f'Seta ligada para a {self.seta}')
        
        
carro1 = Carros('Azul', 2025)
carro1.informacoes()
carro1.ligar()
carro1.ligarSeta('direita')