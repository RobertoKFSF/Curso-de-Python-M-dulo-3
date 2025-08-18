from random import randint
from time import sleep
bot = randint(1,3)
if bot == 1:
    bot = 'PEDRA'
if bot == 2:
    bot = 'PAPEL'
if bot == 3:
    bot = 'TESOURA'
print(''' PEDRA
 PAPEL
 TESOURA''')
while True:
    jogador = str(input('Sua jogada: ')).upper()
    if jogador not in 'PAPELPEDRATESOURA':
        print('Jogada inválida, Digite apenas pedra, papel ou tesoura. ', end="")
    else:
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PÔ')
        sleep(0.2)
        print('=-'*30)
        if jogador == 'PEDRA':
            print('O jogador escolheu Pedra')
        elif jogador == 'PAPEL':
            print('O jogador escolheu Papel')
        elif jogador == 'TESOURA':
            print('O jogador escolheu Tesoura')
        if bot == 'PEDRA':
            print('O bot escolheu Pedra')
        elif bot == 'PAPEL':
            print('O bot escolheu Papel')
        elif bot == 'TESOURA':
            print('O bot escolheu Tesoura')
        if jogador == bot:
            print('EMPATE')
            print('Digite novamente outra jogada, ', end='')
        if jogador == 'PEDRA':
          if bot == 'PAPEL':
            print('O bot ganhou!')
            break
        if jogador == 'PAPEL':
          if bot == 'TESOURA':
            print('O bot ganhou!')
            break
        if jogador == 'TESOURA':
          if bot == 'PEDRA':
              print('O bot ganhou!')
              break
        if bot == 'PEDRA':
            if jogador == 'PAPEL':
                print('O jogador ganhou!')
                break
        if bot == 'PAPEL':
            if jogador == 'TESOURA':
                print('O jogador ganhou!')
                break
        if bot == 'TESOURA':
            if jogador == 'PEDRA':
                print('O jogador ganhou!')
                break