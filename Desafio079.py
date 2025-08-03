num = []
cont = 'S'
if cont == 'S':
    while True:
        n = (int(input('Digite um valor: ')))
        if n not in num:
            num.append(n)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado, não vou adicionar.')
        cont = (str(input('Deseja continuar [S/N]: '))).upper()
        if cont == 'S':
            print()
        else:
            break
print(f'Você digitou os valores {num}')