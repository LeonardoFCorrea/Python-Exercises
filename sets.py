comidas1 = ["Pizza", "Hamburguesa", "Pasta", "Tacos", "Sushi", "Ensalada"]
comidas2 = ["Sushi", "Ensalada", "Pasta", "Pollo", "Pescado", "Ensalada", "Pizza"]

com1 = set(comidas1)
com2 = set(comidas2)


print("Comidas 1:", com1)
print("Comidas 2:", com2)

print("União:", com1 | com2)  # União
print("Interseção:", com1 & com2)  # Interseção
print("Diferença:", com1 - com2)  # Diferença
print("Diferença inversa:", com2 - com1)  # Diferença inversa
print("Diferença simétrica:", com1 ^ com2)  # Diferença simétrica