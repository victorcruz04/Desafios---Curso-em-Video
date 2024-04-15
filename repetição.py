# 46 ANO NOVO
'''
print('\033[1;34mCONTAGEM REGRESSIVA PARA O ANO ANO: \033[m')
from time import sleep
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print('💥💥💥💥💥💥FELIZ ANO NOVO!!!!💥💥💥💥💥💥')
'''
# 47 exibir números pares de 1 ate 50:
'''
print('-' * 25)
for cont in range (1,51):
    if cont % 2 ==0:
        print(cont)
print('END')
print('-' * 25)
'''
# 48 soma de números entre 1 e, multiplos de 3
'''
soma_3 = 0
cont = 0
for cont in range(0,501):
    if cont % 2 == 1:
        if cont % 3 == 0:
            soma_3 += cont
print(f'A soma dos valores impares multiplos de 3 são: {soma_3}.')
'''
# 49 TABUADA 
'''
num = int(input('DIGÍTE UM NÚMERO PARA A TABUADA: '))
for c in range (1,11):
    tabu = num * c
    print(f'{num} X {c} = {tabu}')
print('END')
'''
# 50 soma dos numeros pares:
'''
soma = 0
for c in range(1,7):
    num = int(input('\033[1;31mDIGÍTE UM NÚMERO: \033[m'))
    if num % 2 == 00:
        soma += num
print(f'\033[1;34mSOMA DOS NUMEROS PARES, APENAS : {soma}.\033[m')
'''
# 51 PROGRESSÃO ARITMÉTICA
'''
primeiro_termo = int(input('DIGÍTE O PRIMEIRO TERMO: '))
razao = int(input('DIGÍTE A RAZÃO: '))
decimo = primeiro_termo + (11-1) * razao
for c in range(primeiro_termo,decimo,razao):
    print(c,end=' -> ')
print('END')
'''
# 52 NUMERO PRIMO
'''
num = int(input('Digíte um número inteiro: '))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(i,'Não é primo.')
            break
    else:
        print(i+1,'é primo')
elif num == 1:
    print('não é primo,pois é 1')
elif num == 0:
    print('não é primo, pois é 0')
else:
    print('negativo')
'''
# 53 palíndromo
'''
frase = str(input('DIGÍTE UMA FRASE: ')).lower().strip()
frase_1 = frase.replace(' ','')
a_1 = frase[::-1]
a_2 = a_1.replace(' ','')
if frase_1 == a_2:
    print('\033[34mÉ PALINDROMO \033[m')
else:
    print('\033[31mNÃO É PALINDROMO \033[m')
'''
# 54 maior ou menor idade:
'''
soma_maior = 0
soma_menor = 0
for i in range(1,8):
    nome = int(input('DÍGITE O ANO DO SEU NASCIMENTO: '))
    data = 2024 - nome
    if data > 18:
        soma_maior = soma_maior + 1
    else: 
        soma_menor = soma_menor + 1
print(f'{soma_maior} são maiores de idade.')
print(f'{soma_menor} são menores de idade.')
'''
# 55 maior e menor peso lido
'''
maior = 0
menor = 999
for i in range(1,6):
    peso = int(input('Digíte seu peso, por favor: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'{maior} foi o maior.')
print(f'{menor} foi o menor.')
'''
# 56 media, idade do mais velho e quantidade de mulheres que tem menos de 20 anos.
'''
soma = 0
maior_masculino = 0
qtd = 0
for i in range(1,4):
    nome = input('Digíte seu nome: ')
    idade = int(input('digíte sua idade: '))
    if idade < 105:
            soma = soma + idade
    sex = input('seu sexo, f(feminino) ou m(masculino): ')
    if sex == 'm':
            if idade > maior_masculino:
                maior_masculino = idade
    if sex == 'f':
            if idade < 20:
                qtd = qtd + 1
media = soma / 4
print(f'{media} é a média de idade do grupo.')
print(f'{maior_masculino} a maior idade do masculino.')
print(f'{qtd} é o numero de vezes que as mulheres tem menor que 20 anos')
'''
