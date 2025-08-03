lista = 'Lápis', 1.50, 'Borracha', 2.50, 'Apontador', 3.00, 'Livro', 10.00, 'Caneta', 2.00
print('-' * 30)
print('      LISTA DE COMPRAS')
print('-' * 30)


for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
