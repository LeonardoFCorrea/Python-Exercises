# from rich import print

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def apresentar(self):
#         print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos!')
        
        
# pessoa1 = Pessoa(nome='Leonardo', idade= 25)

# Pessoa.apresentar(pessoa1)

# class Funcionario(Pessoa):
#     def __init__(self, nome, idade, funcao):
#         super().__init__(nome, idade)
#         self.funcao = funcao
    
#     def funcao(self):
#         print(f'Meu nome é {self.nome} e sou {self.funcao}!')
        
# funcionario1 = Funcionario(nome='Ricardo', idade=21, funcao='Operador de Caixa')

# Funcionario.funcao(funcionario1)


# def blocoDeNotas(markdowns):
#     def wrapper(*args, **kwargs):
#         print('Função desejada foi: ')
#         markdowns(*args)

#     return wrapper
    
# @blocoDeNotas
# def negrito(texto):
#     print(f"[bold]{texto}[/bold]")
    
# @blocoDeNotas
# def italico(texto):
#     print(f"[italic]{texto}[/italic]")
    
# @blocoDeNotas
# def h1(texto):
#     print(f"[markdown.h1]{texto}[/markdown.h1]")
    

# negrito("CAFÉÉÉÉÉÉ")
# italico("CAFÉ")
# h1("TEXTO GRANDE!!!")

# # --------------------------

# livro1 = {
#     "livro": "Pequeno Príncipe",
#     "prateleira": "A-1"
# }

# print(f"Título: {livro1.get("livro")}")
# print(f"Prateleira: {livro1.get("prateleira")}")


# ---------------------------

numeros = input('Digite seus números separados por " - " (hífen):')
numerosSplit = numeros.split('-')
print(numerosSplit)
numerosSemEspaco = map(lambda x: x.strip(), numerosSplit)
# for num in numerosSemEspaco:
#     print(num)
numerosFiltroPar = filter(lambda x: int(x) %2 == 0, numerosSemEspaco)
for index, numPar in enumerate(numerosFiltroPar, start=1):
    print(f"{index}: {numPar}")