galera = []
resp = 'S'
dado = []
mai = men = 0
while resp == 'S':
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp != 'S':
        break
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end= '')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]} ')
print(f'O menor peso foi de {men}Kg. Peso de ', end= '')
for p1 in galera:
    if p1[1] == men:
        print(f'{p1[0]} ', end= '')