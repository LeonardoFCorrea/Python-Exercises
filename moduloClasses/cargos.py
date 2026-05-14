import time
from moduloClasses.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, trabalhando):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.trabalhando = trabalhando

    def apresentar(self):
        return (
            f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.cargo}."
        )

    def iniciar_turno(self):
        inicio = time.perf_counter()
        while self.trabalhando:
            tempo_decorrido = time.perf_counter() - inicio
            print(
                f"O(A) {self.cargo} {self.nome} está trabalhando... Tempo decorrido: {tempo_decorrido:.2f} segundos"
            )

            if tempo_decorrido >= 5:  # Simula um turno de trabalho de 5 segundos
                self.trabalhando = False
                print(
                    f"O(A) {self.cargo} {self.nome} terminou o turno de trabalho as {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}."
                )

            time.sleep(1)


class Diretor(Funcionario):
    def __init__(self, nome, idade, cargo, trabalhando, departamento):
        super().__init__(nome, idade, cargo, trabalhando)
        self.departamento = departamento

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, sou {self.cargo} e lidero o departamento da escola."


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou aluno do curso de {self.curso}."


# Anotação: time.perf_counter() devolve o tempo atual do relógio interno do Python, não o tempo “decorrido”.
