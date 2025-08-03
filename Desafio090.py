aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = int(input(f'Média de {aluno['nome']}: '))
print(f'O nome é igual a {aluno['nome']}')
if aluno['media'] >= 7:
    print(f'A nota é igual a {aluno['media']} e ele está média!')
    aluno['situação'] = 'Aprovado'
else:
    print(f'A nota é igual a {aluno['media']} e ele está abaixo da média')
    aluno['situação'] = 'Reprovado'
print(f'O aluno {aluno['nome']} teve média de {aluno['media']} pontos e está {aluno['situação']}!')

