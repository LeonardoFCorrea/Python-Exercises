def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
numero = int(input("Digite seu número para receber o fatorial: "))

res = fatorial(numero)

formatado = f"{res:,}".replace(',', '.')

print(f'O fatorial de {numero} é {formatado}!')