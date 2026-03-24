class Apartamento:
    id = 0
    def __init__(self, comprimento, largura, quartos, suites, cor):
        Apartamento.id += 1
        self.numero = Apartamento.id 
        self.comprimento = comprimento
        self.largura = largura
        self.quartos = quartos
        self.suites = suites
        self.cor = cor
    
    def calcularArea(self):
        area = self.comprimento * self.largura
        print(f'A área do apartamento {self.numero} é de {area} m²')
    
    def adicionarQuartos(self, quartosNovos):
        self.quartos = self.quartos + quartosNovos
        print(f'O apartamento {self.numero} tem {quartosNovos} quartos novos, totalizando {self.quartos}')
    
    def pintarApartamento(self, novaCor):
        self.cor = novaCor
        print(f'O apartamento foi pintado de {self.cor}!')

apto1 = Apartamento(5, 4, 3, 1, 'azul')
print(f'Apartamento {apto1.numero}:')
apto1.calcularArea()
apto1.adicionarQuartos(3)
apto1.pintarApartamento('vermelho')

apto2 = Apartamento(10, 10, 5, 2, 'roxo')
print(f'Apartamento {apto2.numero}:')
apto2.calcularArea()
apto2.adicionarQuartos(2)
apto2.pintarApartamento('verde')
