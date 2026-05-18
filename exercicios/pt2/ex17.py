cidades = ('Vancouver', 'Lisboa', 'Bragança')

cidade = str(input('Digite sua cidade: '))

if cidade in cidades:
    print(f'{cidade} está na lista')
else:
    print(f'{cidade} não está na lista')
    