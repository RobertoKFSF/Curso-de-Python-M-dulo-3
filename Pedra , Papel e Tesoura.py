from random import randint
bot = randint(1,3)
print(''' PEDRA [1]
 PAPEL [2]
 TESOURA [3]''')
while True:
    jogador = int(input('Digite um número: '))
    if 0 < jogador < 4:
        if jogador == 1:
            print('O jogador escolheu Pedra')
        elif jogador == 2:
            print('O jogador escolheu Papel')
        elif jogador == 3:
            print('O jogador escolheu Tesoura')
        if bot == 1:
            print('O bot escolheu Pedra')
        elif bot == 2:
            print('O bot escolheu Papel')
        elif bot == 3:
            print('O bot escolheu Tesoura')
        if jogador == bot:
            print('EMPATE')
            print('Digite novamente outro valor, ', end='')
        if jogador == 1:
          if bot == 2:
            print('O bot ganhou!')
            break
        if jogador == 2:
          if bot == 3:
            print('O bot ganhou!')
            break
        if jogador == 3:
          if bot == 1:
              print('O bot ganhou!')
              break
        if bot == 1:
            if jogador == 2:
                print('O jogador ganhou!')
                break
        if bot == 2:
            if jogador == 3:
                print('O jogador ganhou!')
                break
        if bot == 3:
            if jogador == 1:
                print('O jogador ganhou!')
                break
    else:
        print('Número inválido, Digite 1, 2 ou 3.')