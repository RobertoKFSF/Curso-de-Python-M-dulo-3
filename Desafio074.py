from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print ('Os valores sorteados foram: ', end=' ')
for n in numero:
    print(f'{n}', end=' ')
print(f'\nO maior é {max(numero)}')
print(f'O menor é {min(numero)}')
print('FIM DO PROGRAMA')