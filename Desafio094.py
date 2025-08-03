media = cont = 0
pessoa = {}
pessoas = []
while True:
    while True:
        pessoa['nome'] = str(input('Nome: '))
        break
    sexo = 'j'
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
        if sexo == 'm':
            pessoa['sexo'] = sexo
        else:
            pessoa['sexo'] = sexo
    while True:
        idade = int(input('Idade: '))
        pessoa['idade'] = idade
        media += idade
        break
    while True:
        i = str(input('Quer continuar? [S/N] ')).upper()
        if i not in 'SN':
            print('ERRO! Digite apenas S ou N.')
        else:
            break
    print('-='*30)
    pessoas.append(pessoa.copy())
    if i == 'N':
        break
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade é {media/len(pessoas)} anos')
print('C) As mulher(es) cadastrada(s) foram: ', end = '')
for pos, mulher in enumerate(pessoas):
    if mulher['sexo'] == 'f':
        cont += 1
        print(f'[ {mulher['nome']} ] ', end = ' ')
    elif pos + 1 == len(pessoas):
        if cont == 0:
            print(0, end = ' ')
print()
print('- Lista de pessoas que estão acima da média:')
print('-='*30)
for maior in pessoas:
    if maior['idade'] >= media / len(pessoas):
        print(f'nome = {maior['nome']}; sexo = {maior['sexo']}; idade = {maior['idade']};')

