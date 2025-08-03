palavras = ('banana', 'computador', 'janela', 'livro', 'telefone','mesa', 'cadeira', 'carro', 'papel', 'porta')
for p in palavras:
    print(f'\nNa palavra {p} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

