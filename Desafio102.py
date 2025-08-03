def fatorial(n):

    f = 1
    for c in range(n, 0, -1):
        f *= c
        print(f'{c} ', end='')
        if c>1:
            print(f'x ',end= '')
        if c == 1:
            print(f'= {f}', end='')

fatorial(5)