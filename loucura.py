lista = ('lápis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00,
         'transferidor', 4.20, 'compasso', 9.99, 'mochila', 120.32,
         'canetas', 22.30, 'livro', 34.90)
compras = []
soma = cont = 0

print("="*50)
print(f"{'LISTAGEM DE PREÇOS':^50}")
print("="*50)

for n1, n in enumerate(lista):
    if n1 % 2 == 0:
        print(f"{n.title():.<40} R$",end="")
    if n1 % 2 == 1:
        print(f"{n:>6.2f}")
print("="*50)

r = input("Deseja comprar algo? [Y/N] ").upper()
while r not in "YN":
    r = input("Deseja comprar algo? [Y/N] ").upper()

if r == "Y":
    while True:
        cp = input("Digite o produto: ").lower().strip()
        if cp in lista:
            compras.append(cp)
            compras.append(lista[lista.index(cp) + 1])
        else:
            print(f"O produto {cp} não existe não lista! Verifique a ortografia!")

        r = input("Deseja continuar? [Y/N] ").upper().strip()[0]
        while r not in "YN":
            r = input("Deseja continuar? [Y/N] ").upper().strip()[0]
        if r == "N":
            r = input("Deseja encerrar as compras? [Y/N] ").upper().strip()[0]
            while r not in "YN":
                r = input("Deseja encerrar as compras? [Y/N] ").upper().strip()[0]
            if r == "Y":
                break
    print("=" * 50)
    print(f"{'LISTAGEM DE COMPRAS':^50}")
    print("=" * 50)

    for n1, n in enumerate(compras):
        if n1 % 2 == 0:
            print(f"{n.title():.<40} R$", end="")
            cont = cont + 1
        if n1 % 2 == 1:
            print(f"{n:>6.2f}")
            soma = soma + n
    print("=" * 50)
    print(f"{'QUANT.ITENS ':><40} {'TOTAL TOT':>6}")
    print()
    print(f"{cont:.<40} R${soma:>6.2f}")


else:
    print("Volte sempre!")