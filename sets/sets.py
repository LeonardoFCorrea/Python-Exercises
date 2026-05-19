comidas1 = ["Pizza", "Hamburguesa", "Pasta", "Tacos", "Sushi", "Ensalada"]
comidas2 = ["Sushi", "Ensalada", "Pasta", "Pollo", "Pescado", "Ensalada", "Pizza"]

ex2 = {1, 2, 3, 4, 5, 1, 2} # Criando um Set Diretente e com elementos duplicados
ex2.add(6) # Adicionando um elemento ao Set
ex2.update([7, 8, 9]) # Adicionando múltiplos elementos ao Set
ex2.remove(3) # Removendo um elemento do Set
ex2.discard(10) # Removendo um elemento do Set sem gerar erro se ele não existir
print(ex2) # Imprimindo o Set, os elementos duplicados serão removidos

print('')
print('--------------------------------------------------------')
print('')

com1 = set(comidas1) # Como transformar lista em Set
com2 = set(comidas2) # Como transformar lista em Set


print("Comidas 1:", com1)
print("Comidas 2:", com2)

print("União:", com1 | com2)  # União
print("Interseção:", com1 & com2)  # Interseção
print("Diferença:", com1 - com2)  # Diferença
print("Diferença inversa:", com2 - com1)  # Diferença inversa
print("Diferença simétrica:", com1 ^ com2)  # Diferença simétrica