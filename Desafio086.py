matriz = [[], [], []], [[], [], []], [[], [], []]
for c in range (0,3):
    for i in range (0,3):
        matriz[c][i] = int(input(f'Digite um valor para [{c}, {i}] '))
print('-='*30)
print(f'[  {matriz[0]}  ]')
print(f'[  {matriz[1]}  ]')
print(f'[  {matriz[2]}  ]')