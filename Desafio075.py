u = 0
num = (int(input('Digite um número de 0 a 10: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os números {num}')
print(f'O número 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O número 3 ta na posição {num.index(3)+1}')
else:
    print(f'O número 3 não foi digitado!')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')





