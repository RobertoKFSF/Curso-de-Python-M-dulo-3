def leiadinheiro(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            ok = True
            return float(entrada)
