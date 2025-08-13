time = ('Flamengo', 'Palmeiras', 'Botafogo', 'Bahia', 'Athletico-PR','Grêmio', 'Cruzeiro', 'São Paulo', 'Internacional', 'Bragantino','Fortaleza', 'Atlético-MG', 'Vasco', 'Corinthians', 'Cuiabá','Juventude', 'Vitória', 'Criciúma', 'Atlético-GO', 'Fluminense')
print(time)
print (time[0:5])
print(time[16:])
print(sorted(time))
for pos, c in enumerate (time):
    if c == 'Fluminense':
        print(f"O fluminense está na posição {pos+1}")
        break
print(f'O fluminense está na posição {time.index("Fluminense")+1}')
print('FIM DO PROGRAMA')