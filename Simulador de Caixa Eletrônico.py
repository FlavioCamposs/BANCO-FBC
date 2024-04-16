def linha(frase):
    tam = len(frase) + 4
    print('=' * tam)
    print(f'  \033[1;97m{frase}\033[m')
    print('=' * tam)


#LISTA DAS CORES
c = ['\033[m',          # 0 - sem cores
     '\033[1;91m',      # 1 - vermelho
     '\033[1;92m',      # 2 - verde
     '\033[1;93m',      # 3 - amarelo
     '\033[1;94m',      # 4 - azul
     '\033[1;97m',      # 5 - Branco
]


def titulo(tit, cor=0):
    tam = len(tit) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {tit}')
    print('=' * tam)
    print(c[0], end='')


titulo('BEM VINDO AO BANCO FBC!', 2)


#Saber se o usuário deseja ou não ver as cedulas que estão disponiveis para saque
def comandoInicial():
    while True:
        cedulas = str(input('\033[1;97mDeseja ver as cedulas disponiveis? [S/N]: \033[m')).upper()[0]
        if cedulas == 'S':
            linha('Cédulas disponiveis: 100, 50, 20, 10, 5, 1')
            break
        elif cedulas == 'N':
            break
        else:
            print('Dado invalido! digite apenas S ou N')


comandoInicial()


def comandoDeEntrada():
    return int(input(f'\033[1;97mQual o valor a ser sacado?: \033[m'))


montante = comandoDeEntrada()
print('=' * 46)

#VERIFICAR QUANTAS VEZES EU CONSIGO TIRAR 50 DO VALOR DIGITADO (Se possivel)
cedulaAtual = 100
totalCedula = 0

while True:
    if montante >= cedulaAtual:
        montante -= cedulaAtual
        totalCedula += 1
    else:
        if totalCedula > 0:
            #Ir mostrando quantas cedulas precisa para completar o valor total do saque
            print(f'\033[1;97mTotal de {totalCedula} cédulas de\033[m \033[1;94mR${cedulaAtual}\033[m')

        '''
        Verificar se:
        Tem 50 reais? -> Vai tirando 20 até sobrar apenas 10
        Tem 20 reais? -> Vai tirando 10 até sobrar apenas 5
        Tem 5 reais? -> Vai tirando 1 até não sobrar nada
        '''
        if cedulaAtual == 100:
            cedulaAtual = 50
        elif cedulaAtual == 50:
            cedulaAtual = 20
        elif cedulaAtual == 20:
            cedulaAtual = 10
        elif cedulaAtual == 10:
            cedulaAtual = 5
        elif cedulaAtual == 5:
            cedulaAtual = 1
        totalCedula = 0
        if montante == 0:
            break

#Imprimir uma mensagem de despedida
titulo('Muito Obrigado! Volte sempre ao BANCO FBC!', 1)
