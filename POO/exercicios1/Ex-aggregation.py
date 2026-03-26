class Biblioteca():
    def __init__(self, nome):
        self.nome = nome
        self.estantes = []
        
    def informarcoes(self):
        print(f'Biblioteca: {self.nome}')
            
    def adicionar_Estante(self, estante):
        self.estantes.append(estante)
        
    def listar_Estantes(self):
        for e in self.estantes:
            print(f'Estante {e.numero}')

class Estante():
    def __init__(self, numero):
        self.numero = numero
        self.livros = []
        
    def adicionar_Livro(self, livro):
        self.livros.append(livro)
        
    def listar_Livros(self):
        i = 0
        for l in self.livros:
            i += 1
            print(f'Livro {i}: {l.titulo} - {'Disponível' if l.disponivel else 'Indisponível'}\n-----------------------')
                
        
class Livro():
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

estante1 = Estante('A-1')

biblioteca_Nacional = Biblioteca('Nacional de Passo Fundo')
biblioteca_Nacional.adicionar_Estante(estante1)

livro1 = Livro('Pequeno Príncipe', 'Antoine de Saint-Exupéry', False)
livro2 = Livro('Grande Príncipe', 'Antoine de Saint-Exupéry', True)
livro3 = Livro('Médio Príncipe', 'Antoine de Saint-Exupéry', True)

estante1.adicionar_Livro(livro1)
estante1.adicionar_Livro(livro2)
estante1.adicionar_Livro(livro3)

biblioteca_Nacional.informarcoes()
print('-----------------------')
biblioteca_Nacional.listar_Estantes()
print('-----------------------')
estante1.listar_Livros()