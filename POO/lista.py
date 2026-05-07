# carros_garagem = input("Digite os carros da garagem separados por vírgula: ")

# Convertendo a string em uma lista
# carros_lista = carros_garagem.split(", ")
# print("Carros na garagem:")
# i= 0
# for carro in carros_lista:
#     i+=1
#     print(f"#{i} {carro}")
    
numero = int(input("Digite um número inteiro: "))
for n in range(numero):
    print(f"Contagem: {n+1}")
for i in range(1, n+2):
    print(f"  {i} x {n+1} = {(n+1)*i}")