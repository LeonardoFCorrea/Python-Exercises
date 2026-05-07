set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = {"c", "d", "e"}

set4 = set1.union(set2)  # União
set5 = set1.intersection(set2)  # Interseção
set6 = set1.difference(set2)  # Diferença
set7 = set1.symmetric_difference(set2)  # Diferença simétrica
print("Set 1:", set1)
print("Set 2:", set2)
print("União:", set4)
print("Interseção:", set5)
print("Diferença:", set6)
print("Diferença simétrica:", set7)

# uniao é o conjunto de todos os elementos presentes em ambos os conjuntos, sem duplicatas.
# interseção é o conjunto de elementos que estão presentes em ambos os conjuntos.
# diferença é o conjunto de elementos que estão presentes em um conjunto, mas não no outro.
# diferença simétrica é o conjunto de elementos que estão presentes em um dos conjuntos, mas não em ambos.