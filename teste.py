print('-'*30)
print('LOJA DO ROBERTO'.center(30))
print('-'*30)
valor = 1
total = 0
cont = 1
while valor != 0:
    valor = float(input(f'Produto {cont}: '))
    total += valor
    cont += 1
    if valor == 0:
        break
print(f'O total deu R${total}')
while True:
    dinheiro = float(input('Dinheiro: '))
    if dinheiro >= total:
        break
troco = dinheiro - total
print(f'Troco: R${troco}')
