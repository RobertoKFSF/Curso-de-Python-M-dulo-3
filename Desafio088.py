from random import randint
from time import sleep
lista = []
game = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    game.append(lista[:])
    lista.clear()
    tot +=1
print(f'-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
for i, l in enumerate(game):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE>', '-='*5)