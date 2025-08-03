lista = []
for c in range(0, 5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos+1} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')

