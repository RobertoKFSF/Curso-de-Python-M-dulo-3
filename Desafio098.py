from time import sleep
def cima():
    print('-='*30)
def corr():
    for c in range (1, 11):
        sleep(0.3)
        print(f'{c} ', end= '')
def corre():
    for ca in range (10, -1, -2):
        sleep(0.3)
        print(f'{ca} ', end= '')
def escreva():
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p == 0:
        p += 1
    if i > f:
        p *= -1
    cima()
    print(f'Contagem de {i} até {f-1} de {p} em {p}')
    if f > i:
        f += 1
    if i > f:
        f -= 1
    for u in range(i, f, p):
        sleep(0.4)
        print(f'{u} ', end='')
cima()
print('Contagem de 1 até 10 de 1 em 1')
corr()
print()
cima()
print('Contagem de 10 até 0 de 2 em 2')
corre()
print()
cima()
print('Agora é sua vez de personalizar sua contagem!')
escreva()
print()
cima()
