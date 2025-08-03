def pyhelp():
    print('\033[0;30;41m~'*30)
    print('\033[0;30;41m   SISTEMA DE AJUDA PyHELP \033[0;30;41m')
    print('~' * 30)
def respo():
    t = len(resp) + 33
    print('~'*t)
    print(f'Acessando o manual do comando {resp}')
    print('~'*t)
while True:
    pyhelp()
    resp = str(input('Função ou Biblioteca > '))
    if resp.upper() == 'FIM':
        break
    else:
        print(respo())
        help(resp)