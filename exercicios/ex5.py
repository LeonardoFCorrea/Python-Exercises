def calculos(num1, num2):
    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    expon = pow(num1,num2)
    lista_calculos = [soma, sub, mult, div, expon]
    return print(f"A soma dos números {num1} e {num2} é {soma:.2f}\nA subtração dos {num1} e {num2} números é {sub:.2f}\nA multiplicação dos {num1} e {num2} números é {mult:.2f}\nA divisão dos {num1} e {num2} números é {div:.2f}\nA exponenciação dos números {num1} e {num2} é {expon:.2f}. A lista dos resultados ficou: {lista_calculos}")

num1 = float(input('Digite seu primeiro número para os calculos: '))
num2 = float(input('Digite seu segundo número para os calculos: '))

calculos(num1,num2)