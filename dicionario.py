aluno1 = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia",
    "notas": [8.5, 9.0, 7.5],
}  # Criando um dicionário com chaves e valores
print(aluno1)  # Imprime o dicionário completo
print("")

print(aluno1.values())  # Retorna os valores do dicionário
print("")

print(aluno1.keys())  # Retorna as chaves do dicionário
print("")

print(aluno1.items())  # Retorna os itens do dicionário como tuplas (chave, valor)
print("")

print(aluno1["nome"])  # Acessa o valor associado à chave "nome"
print("")

aluno1["idade"] = 21  # Modifica o valor associado à chave "idade"
aluno1["email"] = "joao@email.com"  # Adiciona um novo par chave-valor ao dicionário
print(aluno1)  # Imprime o dicionário atualizado
print("")

print(      
    "Notas:", aluno1.get("notas")
)  # Acessa o valor associado à chave "notas" usando o método get()
print("")

for valor in aluno1.values():
    print(valor)  # Imprime cada valor do dicionário

print("")

for chave in aluno1.keys():
    print(chave)  # Imprime cada chave do dicionário

print("")

for chave, valor in aluno1.items():
    print(
        f"{chave}: {valor}"
    )  # Imprime cada chave e valor do dicionário no formato "chave: valor"

print("")
