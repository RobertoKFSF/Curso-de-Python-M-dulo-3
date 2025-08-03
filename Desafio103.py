def ficha(a='<desconhecido>', b1=0):
    print (f'O jogador {a} fez {b1} gols no campeonato')

a = str(input('Nome do Jogador: '))
b = str(input('Gols: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    ficha(b1=b)
else:
    ficha(a, b)

