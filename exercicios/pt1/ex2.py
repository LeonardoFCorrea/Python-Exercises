def tintaNecessaria(rendimento, largura, altura):
    area = largura * altura
    tinta = area / rendimento
    return print(f"Você precisará de {tinta:.2f} litros de tinta para pintar a parede.")

rendimento = float(input("Digite o rendimento da tinta (m² por litro): "))
largura = float(input("Digite a largura da parede (m): "))
altura = float(input("Digite a altura da parede (m): "))

tintaNecessaria(rendimento, largura, altura)