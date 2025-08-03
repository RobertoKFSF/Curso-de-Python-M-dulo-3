num = [2, 5, 9, 1]
num[2] = 3
num.insert(2,3)
print(num)
num.append(5)
print(f'Essa lista tem {len(num)} elementos')
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.pop(2)
print(num)
num.remove(5)
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

valores = []
valor = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')
print('Cheguei ao fim da lista!')

for cont in range (0, 5):
    valor.append(int(input('Digite um valor: ')))
print(f'{valor}')

a = [2, 3, 4, 5, 7]
#b = a SE EU USAR APENAS ISSO ELE CRIA LIGAÇÃO, E SE EU MUDAR A LISTA "b" MUDA A LISTA A TAMBEM!
b = a[:] #FORMA CORRETA DE USAR COM FATIAMENTO DE TUDO!
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')