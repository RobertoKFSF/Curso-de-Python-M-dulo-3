matriz = [[], [], []], [[], [], []], [[], [], []]
spar = smai = col = 0
for c in range (0,3):
    for i in range (0,3):
        matriz[c][i] = int(input(f'Digite um valor para [{c}, {i}] '))
print('-='*30)
print(f'[  {matriz[0]}  ]')
print(f'[  {matriz[1]}  ]')
print(f'[  {matriz[2]}  ]')
for c in range (0,3):
    for i in range(0,3):
        if matriz[c][i] % 2 == 0:
            spar += matriz[c][i]
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for c in range (0,3):
    col += matriz[c][2]
print(f'A sina dis valores da terceira coluna é {col}.')
for c in range (0,3):
    if c == 0:
        smai = matriz [1][c]
    elif matriz[1][c] > smai:
        smai = matriz[1][c]
print(f'O maior valor da segunda linha é {smai}')


