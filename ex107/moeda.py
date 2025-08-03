def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxa1=80, taxa2=35):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preco, taxa1 ,True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preco, taxa2,True)}')
    print('-'*30)
