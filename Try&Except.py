carros = ["Gol", "Uno", "Civic"]

try:
    print(carros[3])
except IndexError:
    print("O índice está fora do alcance da lista.")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
try:
    numero = int("abc")
except ValueError:
    print("Não é possível converter a string para um número inteiro.")
try:
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
    
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    
user_input = input("Digite um número para dividir por 2: ")
try:
    result = int(user_input) / 2
except:  # noqa: E722
    print("Something went wrong.")
else:
    print(f"O resultado da divisão é: {result}")
finally:
    print("Este bloco será executado independentemente de ocorrer uma exceção ou não.")