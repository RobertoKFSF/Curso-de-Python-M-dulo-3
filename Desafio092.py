pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['data'] = int(input('Ano de Nascimento: '))
pessoa['ct'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ct'] != 0:
    pessoa['ano'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    print(f'O nome é {pessoa['nome']}')
    print(f'Nasceu em {pessoa['data']}')
    print(f'CTPS tem o valor de {pessoa['ct']}')
    print(f'Foi contratado em {pessoa['ano']}')
    print(f'O salário de {pessoa['nome']} é de R$ {pessoa['salario']}')
else:
    print(f'O nome é {pessoa['nome']}')
    print(f'Nasceu em {pessoa['data']}')
    print(f'{pessoa['nome']} Não tem carteira de trabalho')



