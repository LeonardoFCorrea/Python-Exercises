def apresentar(falar):
    def gritar():
        print('AAAA!!!!')
        falar()
        quatro = 2 + 2
        print(f'DOIS MAIS DOIS É {quatro}')
    return gritar

@apresentar
def gritar2():
    print('BBBB!!!!')

gritar2()