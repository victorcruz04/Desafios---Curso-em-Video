# 66 Quantos números digitados e a soma deles.
'''
num = 0
cont_num = soma_num = 0
while True:
    num = int(input('Digíte um número inteiro( ou 999 p/ sair): '))
    if num == 999:
        break
    cont_num += 1
    soma_num += num
print(f'\033[35mForam {cont_num} números digitado no total.\033[m')
print(f'\033[35mA soma dos números será de {soma_num}.\033[m')
'''
#67 tabuada 3.0
'''
while True:
    num = int(input('Tabuada de qual número? '))
    if num < 0:
        print('Tabuada encerrada, volte sempre!')
        break
    for i in range (0,11):
        print(f'{num} X {i} = {num * i}')
    print('-' * 40)
'''
# 68 par ou impar
'''
import random
cont = 0
while True:
    valor = int(input('Digíte um valor? '))
    p_i = input('Par ou impar?[P/I]').strip().lower()
    ia = random.randint(1,10)
    total = valor + ia
    print('-' * 30)
    print(f'você escolheu {valor} e a IA escolheu {ia}.')
    if p_i == 'p':
        if total % 2 == 0:
            print(f'O total foi {total}: DEU PAR ')
            print('você venceu!')
            print('-'*30)
            cont += 1

        else: 
            print(f'O total foi {total}: DEU IMPAR ')
            print('\033[31mVocê perdeu\033[m')
            print('-'*30)
            print(f'Vitórias consecutivas: {cont}.')
            break

    elif p_i =='i':
        if total % 2 != 0:
            print(f'O total foi {total}: DEU IMPAR ')
            print('Você ganhou')
            print('-'*30)
            cont += 1
        else:
            print(f'O total foi {total}: DEU PAR ')
            print('\033[31mVocê perdeu\033[m')
            print('-'*30)
            print(f'Vitórias consecutivas: {cont}.')
            break
    else:
        print('\033[31minválido\033[m')
        print('-'*30)
'''
#69 cadastro de pessoas (90% feito)
'''
mulher_menos_20anos = 0
homens_cadastrados = 0
mais_18 = 0
while True:
    print(' ' * 5,'CADASTRE UMA PESSOA',' ' * 5)
    print('-' * 50)
    idade = int(input('Digíte sua idade: '))
    if idade > 18 :
        mais_18 += 1
    sexo = input('Digíte seu sexo:[M/F] ').strip().lower()
    
    if sexo == 'f':
        if idade < 20:
            mulher_menos_20anos += 1
    elif sexo == 'm':
        homens_cadastrados +=1
    else:
        print('Inválido')
        break
    dilema = input('Deseja continuar?[S/N]').strip().lower()
    if dilema == 's':
        continue
    elif dilema == 'n':
        break
print('-' * 55)
print(' ' * 10,'FIM DO PROGRAMA',' ' * 10)
print('-' * 55)
print(f'Total de pessoas com mais de 18 anos: {mais_18}.')
print(f'Ao todo, temos {homens_cadastrados} homens cadastrados.')
print(f'E temos {mulher_menos_20anos} mulheres com menos de 20 anos.')
'''  
# 70
'''
tot_gasto = 0
produto_1000 = 0 
menor = 99999
while True :
    print('-' * 30)
    print('LENDO NOME E PREÇO DE PRODUTOS')
    print('-' * 30)
    nome = input('Nome do produto: ')
    preço = float(input('Preço do produto: R$ '))
    tot_gasto += preço
    if preço > 1000:
        produto_1000 += 1
    elif preço < menor:
        menor = preço
        nome1 = nome
        print(nome1)
    while True:
        dilema = input('deseja continuar?:[S/N] ').strip().lower()
        if dilema =='s':
            break
        elif dilema == 'n':
            break
        else:
            print('invalido')
    if dilema == 'n':
        break
print(f'Total gasto: {tot_gasto}.')
print(f'{produto_1000} produtos custam mais de R$1000.00 reais')
print(f'{nome1} produto mais barato.')
'''
#71 Banco Digital
'''
print('-' * 39)
print('|',' ' * 10,'\033[1;34mBanco digital\033[m',' ' * 10,'|')
print('-' * 39)
while True:
    valor = int(input('Informe um valor INTEIRO: '))
    if valor < 0:
        print('Informe outro valor')
    resu = valor
    ced = 50
    tot = 0
    while True:
        if resu > ced:
            resu -= ced
            tot += 1
        else:
            if tot > 0:
                print(f'total de {tot} cedulas de {ced}.')
            if resu == 50:
                ced = 20
            elif resu == 20:
                ced = 10
            elif resu == 10:
                ced = 1
            tot = 0
            if resu == 0:
                break
'''

