# PRÁTICA DA AULA DE LISTAS
'''
tupla = (1,2,3,4,5)  não posso modificar o conteúdo das tuplas
print(tupla)
'''
'''
lista = [3,9,4,7,1]
print('conteúdo:',lista)
print('Buscar um elemento:',lista[2])
lista[2] = 3
print('Modificando um elemento:',lista)
lista.append(7)
print('Adicionando um número:',lista)
lista.sort(reverse = True)
print('ordenando os números:',lista)
print(f'Essa lista tem {len(lista)} elementos.')
lista.insert(0,8)
print('modificando elementos:',lista)
lista.pop()
print(lista)
if 1 in lista:
    lista.remove(3)
else:
    print('Não encontrei esse número')
print(lista)
'''
'''
valores = []
for contagem in range(0,5):
    valores.append(int(input('Digíte um valor: ')))
for posição,valor in enumerate(valores):
    print(f'Na posição {posição} o valor é {valor}.')
'''
'''
a = [2,3,4,7]
b = a[:] # fazendo uma cópia da a, pois em lista existe ligamento
b[2] = 8
print(a)
print(b)
#----------------------------------------------------------------------------
'''
#78(90% completo)
'''
lista = []
maior = 0
menor = 0 
for cont in range(0,5):
    lista.append(int(input(f'Digíte um valor para a posição  {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'Você digitou os valores {lista}.')
print(f'O maior valor digitado foi {maior} na posição,',end='')
for pos,valor in enumerate(lista):
    if valor == maior:
        print (pos,end='...')
print(f'\nO menor valor foi {menor},nas posições,',end='')
for posi, valor in enumerate(lista):
    if valor == menor:
        print(posi,end='...')
'''
# 79
'''
lista = []
while True:
    num = int(input('Digíte um valor: '))
    if num not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(num)
    else: 
        print('Valor duplicado,não vou adicionar.')

    r = str(input('Deseja continuar?: '))
    if r in 'Nn':
        break
lista.sort()
print(f'você digitou os valores {lista}')
'''
#80
'''
lista = []
maior = 0
menor = 0
for c in range(0,5):
    num = int(input('Digíte um número:(0 para sair) '))
    if c == 0 or num > lista[-1]:
        print('Adicionado ao final da lista.')
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print(lista)
'''
#81
'''
lista = []
num = 1
cont = 0
while num != 0:
    num = int(input('Digíte um número:(0 para parar) '))
    lista.append(num)
    cont += 1
print(lista)
if 5 in lista:
    print('5 está na lista')
else:
    print('5 não está na lista.')

lista.sort(reverse = True)
print(f'Foram digitados {cont} números.')
print(f'Descrescente: {lista}.')
'''
#82
'''
lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digíte um número: '))
    lista.append(num)
    dilema = input('Deseja continuar?[S/N] ').strip().lower()
    if dilema == 's':
        continue
    elif dilema == 'n':
        break 
print(f'Lista completa:{lista}')
print('-' * 40)
for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print(f'Lista dos pares {lista_par}.')
print('-' * 10)
print(f'Lista dos ímpares{lista_impar}.')
print('-' * 40)
'''
#83
'''
ex = str(input('digíte uma expressão: '))
pilha = []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
print(pilha)
print(len(pilha))
if len(pilha) == 0:
    print('Correta')
else:
    print('incorreta')
=========================================LISTA(PARTE 2)==============================================
'''
# TESTE
'''
teste = []
teste.append('victor')
teste.append(20)
galera = []
galera.append(teste[:])
teste[0]= 'lucia'
teste[1] = 21
galera.append(teste[:])
print(galera)
'''
'''
#pessoas = [['Victor',20],['João',20],['Pedro',20],['Letícia',17]]
#print(pessoas[0])
#print(pessoas[0][0])
#print(pessoas[0][1])
#for pessoa in pessoas:
    #print(pessoa)
    #print(pessoa[0])
    #print(pessoa[1])
pessoas = list()
dados = list()
totmaior = 0

totmenor = 0
for contador in range(0,3):
    dados.append(str(input('nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)

for idade in pessoas:
    if idade[1] >= 18:
        print(f'{idade[0]} é maior de idade.'.capitalize())
        totmaior +=1
    else:
        print(f'{idade[0]} é menor de idade.'.capitalize())
        totmenor += 1

print(f'{totmaior} são maiores e {totmenor} são menores')
'''
#84(90% completo)
'''
temp = []
princ = []
maior = men = 0
while True:
    temp.append(str(input('NOME: ')))
    temp.append(float(input('PESO: ')))
    if len(princ) == 0:
        maior = men = temp[1]
    else:
        if temp[1]> maior:
            maior = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('QUER CONTINUAR? [S/N] '))
    if resp in 'Nn':
        break
print(f'os dados foram {princ}')
print(f'ao todo, você cadastrou {len(princ)} pessoas')
print(f'o maior foi de {maior} e o menor foi de {men}.')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
'''
#85
'''
dados = list()
numeros = list()
pares = list()
impares = list()
for cont in range(0,7):
    dados.append(int(input(f'Digíte o {cont + 1 }° número: ')))
    numeros.append(dados[:])
    dados.clear()
for num in numeros:
    if num[0] % 2 == 0:
        pares.append(num[0])
    if num[0] % 2 == 1:
        impares.append(num[0])
print(f'Pares: {pares}.')
print(f'Impares {impares}.')
'''
#86 Matriz
'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para [{l},{c}] '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
'''
#87
'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
scol = 0
maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'valor para:[{l},{c}] '))
        if matriz[l][c] % 2 ==0:
            pares.append(matriz[l][c])

for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
    print()

print(f'A soma dos números pares são de {sum(pares)}.')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna {scol}')
for c in range(0,3):
    if c ==0:
        maior = matriz[1][c]
    elif matriz[l][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha {maior} ')
'''
#88
'''
from random import randint
lista = list()
jogos = list()
quant = int(input('Quantos jogos você jogará? '))
tot = 0
while tot <= quant:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
    for i,l in enumerate(jogos):
        print(f'numeros sorteados {l}')
    '''
#89
'''
ficha = list()
while True:
    name = str(input('Seu nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Sua segunda nota: '))
    media = (nota1 + nota2)/2
    ficha.append([name,[nota1,nota2],media])
    resp =str(input('Deseja continuar? '))
    if resp in 'Nn':
        break
print(f'{'No':<4}{'nome':<10}{'media':>8}')
print('-='*30)
for pos,fich in enumerate(ficha):
    print(f'{pos:<4}{fich[0]:<10}{fich[2]:>8}')
print('-='*30)
while True:
    quem = int(input('POS de quem você deseja ver as notas 1 e 2:[999 p/ sair] '))
    if quem == 999:
        print('saindo...')
        break
    if quem <= len(ficha)-1:
        print(f'notas de {ficha[quem][0]} são {ficha[quem][1]}')
print('volte sempre!')
'''