
temperatura = float(input("Digite a temperatura em Celsius: "))

# Solução Simples

# if temperatura < 0 or temperatura < 48:
#     print("Precisa cozinhar um pouco mais.")

# elif temperatura <= 49:
#     print("Está selada.")

# elif temperatura <= 55:
#     print("Ao ponto para mal.")

# elif temperatura <= 61:
#     print("Ao ponto.")

# elif temperatura <= 66:
#     print("Ao ponto para bem.")

# elif temperatura <= 72:
#     print("Bem passada.")

# else:
#     print("Bem passada.")

# Solução com In Range

if temperatura < 48:
    print("Precisa cozinhar um pouco mais.")

elif temperatura in range(48, 53):
    print("Está selada.")

elif temperatura in range(54, 59):
    print("Ao ponto para mal.")

elif temperatura in range(60, 64):
    print("Ao ponto.")

elif temperatura in range(65, 70):
    print("Ao ponto para bem.")

elif temperatura > 71:
    print("Bem passada.")