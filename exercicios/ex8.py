frutas = ['Maçã', 'Banana', 'Melão']
vegetais = ['Alface', 'Rúcula', 'Couve']
combinacoes = []

for fruta in frutas:
    for vegetal in vegetais:
        print(f"{fruta} e {vegetal}")
        combinacoes.append([fruta, vegetal])
    
print(combinacoes)