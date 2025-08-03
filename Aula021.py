from time import sleep
#help(input)
def contador(i, f, p):
    """-> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Roberto Kleber"""
    c = i
    while c <= f:
        print(f'{c} ', end= '')
        c += p
    print('FIM!')
def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma vale {s}')


contador(0, 100, 10)
somar(3, 2, 5)
somar(8, 4)
somar(c=4, a=2)
somar()
help(contador)
print()

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()

#Não funciona porque nao ta dentro de def
#print(f'No programa principal, x vale {x}')
print()
def testi(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5
testi(a)
print(f'A fora vale {a}')
# ERRO! print(f'B fora vale {b}')
# ERRO! print(f'C fora vale {c}')
print()
#da pra mudar com a escrevendo global
def testin(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5
testin(a)
print(f'A fora vale {a}')
print()
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
    print()
    return s
r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Meus calculos deram {r1}, {r2} e {r3}')
print()
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print()
print(f'Os resultados são {f1}, {f2} e {f3}')
print()
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um numero: '))
if par(num):
    print('É par')
else:
    print('Não é par!')