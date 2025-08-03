lista = []
cont = 'S'
while cont == 'S':
    lista.append(int(input('Digite um valor: ')))
    cont = (str(input('Quer continuar? [S/N] '))).upper()
    if cont != 'S':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')




