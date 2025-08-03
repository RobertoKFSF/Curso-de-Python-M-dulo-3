teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(teste)

galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 14], ['Maria', 45]]
print(galera1)
print(galera1[0])
print(galera1[2][1])
for p in galera1:
    print(p)
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade')

kblz = []
dado = []
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    kblz.append(dado[:])
    dado.clear()
print(kblz)
totmai = 0
totmen = 0
for p in kblz:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmen} menores de idade e {totmai} maiores de idade!')