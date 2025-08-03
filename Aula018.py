pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} e o sexo é {pessoas['sexo']}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for g in pessoas.values():
    print(g)
print()
for j in pessoas.items():
    print(j)
print()
for i, u in pessoas.items():
    print(f'{i} = {u}')
print()
pessoas['nome'] = 'Leandro'
print(pessoas)
print()
pessoas['peso'] = 98.5
print(pessoas)
print()
del pessoas['sexo']
#print(pessoas['sexo']) DA ERRO POIS FOI DELETADO

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print()
print(estado2)
print()
print(brasil)
print()
print(brasil[0])
print()
print(brasil[0]['uf'])
print()
estado = {}
brazil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(estado.copy())
print(brazil)
for e in brazil:
    print(f'O estado {e['uf']} com a sigla {e['sigla']}')
for j in brazil:
    for k, v in j.items():
        print(f'O campo {k} tem valor {v}')
    for w in j.values():
        print(v)

