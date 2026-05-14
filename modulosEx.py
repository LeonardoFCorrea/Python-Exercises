from moduloClasses.cargos import Funcionario, Diretor, Aluno
from moduloClasses.pessoa import Pessoa

pessoa = Pessoa("Leonardo", 30)
funcionario = Funcionario("Maria", 28, "Professora", True)
diretor = Diretor("Carlos", 45, "Diretor", "Administração", True)
aluno = Aluno("Ana", 20, "Engenharia")

print(f"{pessoa.apresentar()}\n --------")
print(f"{funcionario.apresentar()}\n --------")
print(f"{diretor.apresentar()}\n --------")
print(f"{aluno.apresentar()}")

funcionario.iniciar_turno()
diretor.iniciar_turno()