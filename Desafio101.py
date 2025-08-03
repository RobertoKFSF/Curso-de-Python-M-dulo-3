def voto(n=0):
    from datetime import date
    atual = date.today().year
    idade = atual - v
    if 65 > idade >= 18:
        return f'Com {idade}. VOTO OBRIGÁTORIO!'
    elif idade > 64 or 16 <= idade < 18:
        return f'Com {idade}. VOTO OPCIONAL!'
    if idade < 16:
        return f'Com {idade}. NÃO VOTA!'
v = int(input('Seu ano de nascimento: '))
print(voto(v))
