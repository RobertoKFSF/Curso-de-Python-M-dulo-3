jogador = {}
partidas = []
jogadores = []
resp = 'S'
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partida'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for p in range (0, jogador['partida']):
        partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
    print('=-'*30)
    jogador['total'] = sum(partidas)
    jogador['gols'] = partidas[:]
    jogadores.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
    jogador.clear()
    partidas.clear()
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, p in enumerate(jogadores):
    print(f'{i} {p['nome']}    {(jogadores[i])['gols']}    {p['total']}')
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(jogadores)-1:
        print('=-' * 30)
        print(f'{jogadores[opc]['nome']}    {(jogadores[opc])['gols']}    {jogadores[opc]['total']}')
        print('=-' * 30)
    else:
        print('Use um código válido!')
        print('=-' * 30)