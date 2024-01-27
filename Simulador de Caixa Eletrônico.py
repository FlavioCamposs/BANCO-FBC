print('=' * 30)
print('{:^30}'.format('BEM VINDO AO BANCO FBC!'))
print('=' * 30)

#Saber se o usuário deseja ou não ver as cedulas que estão disponiveis para saque
while True:
    cedulas = str(input('Deseja ver as cedulas disponiveis? [S/N]: ')).upper()[0]
    if cedulas == 'S':
        print('=' * 30)
        print('Cédulas disponiveis: 100, 50, 20, 10, 5, 1')
        print('=' * 30)
        break
    elif cedulas == 'N':
        break
    else:
        print('Dado invalido! digite apenas S ou N')


valor = int(input('Qual o valor a ser sacado?: '))
montante = valor

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
            print(f'Total de {totalCedula} cédulas de R${cedulaAtual}')

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
print('=' * 48)
print('{:^48}'.format('Muito Obrigado! Volte sempre ao BANCO FBC!'))
print('=' * 48)