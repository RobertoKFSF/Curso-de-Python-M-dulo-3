num = [9999999999999999999999999999999999999999999999999]
for c in range(0,5):
    n = (int(input('Digite um número: ')))
    if n < num [0]:
        num.insert(0, n)
        print(f'O número {n} foi adicionado na posição 1')
    elif n < num[1]:
        num.insert(1, n)
        print(f'O número {n} foi adicionado na posição 2')
    elif n < num[2]:
        num.insert(2, n)
        print(f'O número {n} foi adicionado na posição 3')
    elif n < num[3]:
        num.insert(3, n)
        print(f'O número {n} foi adicionado na posição 4')
    elif n < num[4]:
        num.append(n)
        print(f'O número {num} foi adicionado ao fim da lista.')
num.remove(9999999999999999999999999999999999999999999999999)
print(num)
