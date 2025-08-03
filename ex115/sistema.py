from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Cadastrar pessoa', 'Listar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerarquivo(arq)
    elif resposta == 3:
        print('\033[31mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)