lista = []
cont = 'S'
par = []
impar = []
while cont == 'S':
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = (str(input('Quer continuar? [S/N] '))).upper()
    if cont != 'S':
        break
par.sort()
impar.sort()
lista.sort()
print(f'Os números digitados foram {lista}')
print(f'Os números pares digitados foram {par}')
print(f'Os números ímpares digitados foram {impar}')