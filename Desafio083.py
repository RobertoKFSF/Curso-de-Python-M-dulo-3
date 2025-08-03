expr = str(input('Digite sua expressão: '))
n = []
for simb in expr:
    if simb == '(':
        n.append('(')
    elif simb == ')':
        if len(n) > 0:
            n.pop()
        else:
            n.append(')')
            break
if len(n) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

