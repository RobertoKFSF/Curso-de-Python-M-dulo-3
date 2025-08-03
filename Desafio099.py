from time import sleep

def tot(*num):
    cont = tot = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            tot = valor
        elif valor > tot:
            tot = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {tot}')
print()
tot(2, 4, 7, 1)
tot(9, 4, 2, 5, 8)
tot(3, 9, 0)
tot(2, 0)
tot()


