def mostralinha():
    print('-='*30)
print()
mostralinha()
print('Olar')
mostralinha()
print('Jorel')
mostralinha()
print()
def titulo(txt):
    print('-='*30)
    print(txt)
    print('-='*30)
titulo('PYTHON')
titulo('FLUZAO')
titulo('THE')
titulo('CHAMP')

#Loucura
#print()
#a = 4
#b = 5
#s = a + b
#print(s)
#a = 8
#b = 9
#s = a + b
#print(s)
#a = 2
#b = 1
#s = a + b
#print(s)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)
print()
soma(4, 5)
soma(8, 9)
soma(2, 1)
print()

def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print(num)
    print()
    print(f'Recebi os valores {num} e são ao todo {len(num)} valores')
contador (2, 1, 7)
contador (8, 0)
contador (4, 4, 7, 6, 2 )

def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos]*=2
        pos +=1
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
print()
def k(* v):
    si = 0
    for kk in v:
        si += kk
    print(f'Somando os valores {v} temos {si}')
k(5, 2)
k(9, 8, 5)