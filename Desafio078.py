num = []
mai = 0
men = 0
for a in range(0,5):
    num.append(int(input(f'Digite o valor na posição {a+1}: ')))
    if a == 0:
        mai = men = num [a]
    else:
        if num[a] > mai:
            mai = num[a]
        if num[a] < men:
            men = num[a]
print(f'Os números digitados foram {num}')
print(f'O maior número é {mai} nas posições ', end= '')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i+1}... ', end= '')
print()
print(f'O menor número é {men} nas posições ', end= '')
for i, v in enumerate(num):
    if v == men:
        print(f'{i+1}... ', end= '')
print()