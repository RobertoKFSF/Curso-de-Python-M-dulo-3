numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=(' '))
print (numero[num])
print('FIM DO PROGRAMA')
