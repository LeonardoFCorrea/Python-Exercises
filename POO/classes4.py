class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        
    def mostrarInformacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')
        
    def promover(self, novoCargo):
        print(f'{self.nome} foi promovido(a) para {novoCargo}')
        
    def atualizarIdade(self, novaIdade):
        if(novaIdade > self.idade):
            print(f'Atualizando a Idade de {self.idade} para {novaIdade}')
        else:
            print(f'A nova idade tem que ser maior que a idade atual')
            

colaborador1 = Pessoa('Leonardo', 25, 'Programador Júnior')
colaborador2 = Pessoa('David', 22, 'Programador Júnior')

colaborador1.mostrarInformacoes()
colaborador1.promover('Programador Pleno')
colaborador1.atualizarIdade(26)

print('---------------------')

colaborador2.mostrarInformacoes()
colaborador2.promover('Programador Pleno')
colaborador2.atualizarIdade(23)