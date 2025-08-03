jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partida'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for p in range (0, jogador['partida']):
    partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
print('=-'*30)
jogador['total'] = sum(partidas)
jogador['gols'] = partidas[:]
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*30)
n = len(partidas)
print(f'O jogador {jogador['nome']} fez {jogador['partida']} jogos.')
for i in range(0, n):
    print(f'   => Na partida {i+1} fez {partidas[i]} gols')
print(f'Ele fez um total de {jogador['total']} gols')


