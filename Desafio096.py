def area():
    l = (float(input('LARGURA (m): ')))
    c = (float(input('COMPRIMENTO (m): ')))
    t = l * c
    print(f'A área de um terreno {l} x {c} é de {t}m²')
def cabecalho():
    print('   Controle de Terrenos')
    print('-'*30)

#programa principal
cabecalho()
area()
