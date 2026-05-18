altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

while altura != 'cancelar':
    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
    elif imc < 25:
        print(f"Seu IMC é {imc:.2f}. Você está com o peso normal.")
    elif imc < 30:
        print(f"Seu IMC é {imc:.2f}. Você está com sobrepeso.")
    else:
        print(f"Seu IMC é {imc:.2f}. Você está com obesidade.")

    altura = input("Digite sua altura em metros (ou 'cancelar' para sair): ")
    if altura == 'cancelar':
        break
    peso = float(input("Digite seu peso em kg: "))
