lista = [[[]]]
x = 0
y = 0
resp = 'S'
while resp == 'S':
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    lista[x][y].append(nome)
    if y == 2:
        x += 1
        y = 0
    else:
        y += 1
    lista[x][y].append(n1)
    if y == 2:
        x += 1
        y = 0
    else:
        y += 1
    lista[x][y].append(n2)
    resp = str(input('Deseja Continuar? [S/N] ')).upper()
print(lista)
