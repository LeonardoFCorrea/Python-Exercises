class Carro():
    nome: str
    marca: str
    km: int
    
    def Kilometers(nome, km):
        return f'{nome} can reach {km} Km/s'
    
    def Comentarios():
        return f'Hello World!'

class Pessoa(Carro):
    nome: str
    cpf: str
    
    def Comentarios(nome):
        return f'Hello {nome}'

carro1 = Carro()
carro1.marca = 'Lamborghini'
carro1.nome = 'Aventador'
carro1.km = 240
pessoa1 = Pessoa()
pessoa1.nome = 'Leonardo'
pessoa1.cpf = '03850437086'

printPessoa1 = Pessoa.Comentarios(pessoa1.nome)
print(printPessoa1)

print(Carro.Kilometers(carro1.nome, carro1.km))