from random import randint
from time import sleep
numeros = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
def sorteia():
    print(f'Sorteando os 5 valores da lista: ', end = '')
    for c in numeros:
        sleep(0.3)
        print(f'{c} ', end= '')
    print('PRONTO!')
def somapar():
    print()
    t = 0
    for s in numeros:
        if s % 2 == 0:
            t += s
    print(f'Somando os valores pares de {numeros}, temos {t}')
print(numeros)
sorteia()
somapar()
