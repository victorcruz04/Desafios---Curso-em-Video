#57 SEXO CERTO
'''
a = 1
while a == 1 :
    sex = input('Qual é seu sexo?[F/M]').strip().lower()
    if sex == 'f' or sex == 'm':
        print('\033[1;34mPROSSEGUINDO\033[m')
        break
    else:
        print('\033[1;31mTENTE NOVAMENTE\033[m')
'''
#58 Adivinhe o numero 2.0
'''
a = 1
tentativas = 0
while a > 0:
    import random
    from time import sleep
    pense = int(input('Adivinhe um número(de 0 a 5) que eu pensei!: '))
    print('PROCESSANDO...')
    sleep(2)
    a = random.randint(1,5)
    if pense == a:
        print(f'O que eu pensei {a}.\nO que você colocou {pense}')
        print('Parabéns, acertou!')
        print(f'Precisou de {tentativas} tentativas.')
        break
    else:
        print(f'O que eu pensei {a}.\nO que você colocou {pense}')
        print('Errou!')
        tentativas += 1
'''
#59 menu de opções
'''
print('--------MENU--------')
v1 = float(input('Digíte o 1°valor: '))
v2 = float(input('Digíte o 2°valor: '))
print('-' * 16)
a = 1
maior = 0
while a > 0:
    print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR  \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA' )
    qual = int(input('Escolha um número: '))
    if qual == 5:
        print('Saindo...')
        break
    elif qual == 1:
        print(f'A soma de {v1} e {v2} será de {v1 + v2}.')
    elif qual == 2:
        print(f'A multiplicação de {v1} e {v2} será de {v1 * v2}.')
    elif qual == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'O maior número é {maior}.')
    elif qual == 4:
        v1 = float(input('Digíte o 1°valor: '))
        v2 = float(input('Digíte o 2°valor: '))
    else:
        print('\033[31mDIGITE NOVAMENTE\033[m')
'''
#60 fatorial
'''
num = int(input('Digíte um número: '))
num1 = num
i = 1
a = 1
while num >= i:
    print(num,end ='\033[34m x \033[m' if num>1 else ' = ')
    a *= num
    num -= 1 
print(f'\nO fatorial de {num1} será de {a}.')
'''
# 61 PA com while
'''
primeiro_termo = int(input('DIGÍTE O PRIMEIRO TERMO: '))
razao = int(input('DIGÍTE A RAZÃO: '))
decimo = primeiro_termo + (10-1) * razao
atual = primeiro_termo
while(atual <= decimo):
    print(atual,end='\033[36m -> \033[m'if atual < decimo else '')
    atual += razao
'''
#62 PA APRIMORADO
'''
primeiro_termo = int(input('DIGÍTE O PRIMEIRO TERMO: '))
razao = int(input('DIGÍTE A RAZÃO: '))
decimo = primeiro_termo + (10-1) * razao
atual = primeiro_termo
i = 1
while(atual <= decimo):
    print(atual,end='\033[1;31m -> \033[m' if atual<decimo else '.')
    atual += razao
while i>0:
    plus = (input('\nDeseja adicionar mais termos? [S/N]: ')).strip().lower()
    if plus == 's':
        plus_1 = int(input('Quais?: ' ))
        i = 0
        while i < plus_1:
            print(atual,end = '\033[1;31m -> \033[m')
            atual += razao
            i += 1
        print('END')
    elif plus == 'n':
        break
    else: 
        print('INVÁLIDO')
'''
#63 fibonatti
'''
num = int(input('Digíte um número: '))
cont = 0
a = num
print(a,end='\033[1;31m -> \033[m')
b = num + 1
print(b,end='\033[1;31m -> \033[m')
while cont <= 7:
    fibo = a + b
    a = b
    b = fibo
    print(fibo,end='\033[1;31m -> \033[m' if cont < 7 else '.')
    cont += 1
'''
#64 quantos números fooram digítados e a soma desses números:
'''
i = 0
cont = 0
soma = 0
a = 999
while i != a:
    i = int(input('Digíte um número: '))
    if i == a:
        break
    else:
        cont += 1
        soma = soma + i
print(f'Foram digitados {cont} números.')
print(f'A soma é de {soma}.')
print('~'*30)
'''
#65 descobrir o menor, maior valor e a média.
'''
i = 1
soma = 0
cont = 0
maior = 0
menor = 999999
while i > 0:
    num = int(input('Digíte um número: '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'\033[34mMenor valor: {menor}, Maior valor: {maior}\033[m.')
print(f'\033[34mA média dos {cont} números será de {soma/cont}\033[m.')
sn = input('Deseja continuar?[S/N]').strip().lower()
while sn != 'n':
    num = int(input('Digíte um número: '))
    if num == 999:
        break
print(f'Menor valor: {menor}, Maior valor: {maior}.')
print(f'A média dos {cont} números será de {soma/cont}.')
'''