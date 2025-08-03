from ex107 import moeda

p = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p, False))}')
print(f'O dobro de {moeda.moeda(p)} é {(moeda.dobro(p, True))}')
print(f'Aumentando 10% de {moeda.moeda(p)}, temos {(moeda.aumentar(p, 10, True))}')
print(f'Reduzindo 14% de {moeda.moeda(p)}, temos {(moeda.diminuir(p, 14, True))}')