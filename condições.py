#28 
'''
import random
from time import sleep
pense = int(input('digíte um número(de 0 a 5) que seja igual ao que eu pensei!: '))
print('PROCESSANDO...')
sleep(3)
a = random.randint(1,5)
if pense == a:
    print(f'O que eu pensei {a}.\nO que você colocou {pense}')
    print('Parabéns, acertou!')
else:
    print(f'O que eu pensei {a}.\nO que você colocou {pense}')
    print('Errou!')
'''
#29
'''
km = float(input('Digíte a velocidade do carro: '))
print(f'Velocidade do carro {km}km/h.')
if km > 80:
    print(f'Você foi multado!, você andou acima de 80 km\h. \npor isso sua multa sera de R${(km - 80) * 7:.2f}.\nPreste atenção!')
else:
    print('sem multas.')
'''
'''
# 30 par ou impar
num = int(input('Digíte um número INTEIRO: '))
if num % 2 == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é IMPAR.')
'''
# 31 viagem
'''
dist = int(input('Me informe a distância da viagem em KM\h, por favor: '))
if dist <= 200:
    print(f'Pagará R${dist * 0.50:.2f} reais para esta viagem')
else: 
    print(f'Pagará R${dist * 0.45:.2f} reais para esta viagem.')
'''
# 32 ano bissexto 
'''
ano = int(input('Ano que você está: '))
if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é ano bissexto.')
else:
    print(f'O ano {ano} não é ano bissexto.')
'''
# 33 maior e menor
'''
n1 = float(input('Digíte um numero: '))
n2 = float(input('Digíte um número: '))
n3 = int(input('Digíte um número: '))
if n1 > n2 and n3:
    print(f'O maior é {n1:.1f}.')
if n2 > n3 and n1:
    print(f'o maior é {n2:.1f}.')
if n3 > n1 and n2:
    print(f'O maior é {n3:.1f}.')
print('-' * 20)
if n1 < n2 and n3:
    print(f'O menor é {n1:.1f}.')
if n2 < n1 and n3:
    print(f'O menor é {n2:.1f}.')
if n3 < n2 and n1:
    print(f'O menor é {n3:.1f}.')
'''
# 34 aumento de salario
'''
salario = float(input('Digíte seu salário: '))
if salario < 1250:
    print(f'seu salário com o aumento será de R${salario + (salario * 15) / 100:.2f} reais.')
else:
    print(f'Seu salário com o aumento será de R${salario + (salario * 10) / 100:.2f} reais.')
'''
# 3 se retas podem formar um triângulo
'''
a = int(input('Digíte o comprimento de uma reta:  '))
b = int(input('Digíte o comprimento de uma reta: '))
c = int(input('Digíte o comprimento de uma reta: '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('\033[1;31mNao pode formar triângulo.\033[m')
else:
    print('\033[1;34mpode formar triângulo.\033[m')
'''
# MUNDO 2 condições aninhadas:
'''
nome = input('Qual é seu nome? ')
if nome == 'Victor' or nome == 'João' or nome == 'paulo' or nome == 'Valcir':
    print('lindo Nome!!')
elif nome == 'thaiss carla':
    print('GORDA')
elif nome == 'carlinhos' or nome == 'toquinho':
    print('beleza')
else:
    print('nome feio kkkk')
print(f'Tenha um boa dia {nome}!, apesar de bom quem faz é você.') 
'''
# 36 Empréstimo bancário
'''
print('-' * 60)
print('Precisamos de algumas informações para sabermos se você esta opto \npara fazer o empréstimo bancário, para a compra de um imóvel')
valor_casa = float(input('\033[34mDigíte o valor do imóvel :R$ \033[m'))
salario_comprador = float(input('\033[34mDigíte sua renda mensal:R$ \033[m'))
anos_para_pagar = int(input(f'\033[34mEm quantos anos deseja para pagar o imóvel de R${valor_casa:.2f}: \033[m'))
prestacao_mensal = (valor_casa / anos_para_pagar)/12
trinta_porcento_salario = (salario_comprador  * 30) / 100
print(f'prestação mensal R${prestacao_mensal:.2f}')
if prestacao_mensal > trinta_porcento_salario: # Se a prestação mensal for maior que 30% do salario,empréstimo negado.
    print('\033[31mEMPRÉSTIMO NEGADO \033[m')
else:
    print('\033[34mEMPRÉSTIMO APROVADO \033[m')
'''
#38
'''
num_01 = int(input('\033[34mDigíte um número inteiro: \033[m'))
num_02 = int(input('\033[34m um número inteiro: \033[m'))
if num_01 > num_02 :
    print('O primeiro valor é maior.')
elif num_02 > num_01:
    print('O segundo valor é o maior.')
else:
    print('Os dois são iguais.')
'''
#39
'''
ano_nascimento = int(input('informe seu ano de nascimento: '))
if ano_nascimento > 2006:
    print(f'ainda irá se alistar, falta {abs((2024 - ano_nascimento) - 18)} para se alistar')
elif ano_nascimento == 2006:
    print('Já é hora de se alistar!')
else:
    print(f'Já passou da hora de se alistar!! passou {(2024 - ano_nascimento) - 18} anos para se alistar.')
'''
#40
'''
print('\033[31mSITUAÇÃO DA NOTA DO ALUNO: \033[m')
nota_01 = float(input('Digíte sua 1º nota: '))
nota_02 = float(input('Digíte sua 2º nota: '))
media = (nota_01 + nota_02) / 2
if media >= 5 and media <= 6.9:
    print('\033[1;33;40mRECUPERAÇÃO \033[m')
elif media < 5:
    print('\033[1;31;40mREPROVADO \033[m')
else:
    print('\033[1;32;40mAPROVADO \033[m')
'''
#41
'''
print('\033[36mNÍVEL DO NADADOR!\033[m')
i = 1
while i > 0:
    from datetime import date
    ano_atual = date.today().year
    ano_nascimento_nadador = int(input('Informe o ano de nascimento: '))
    idade_nadador = ano_atual - ano_nascimento_nadador
    if idade_nadador <= 9:
        print('MIRIM' )
    elif idade_nadador > 9 and idade_nadador <=14:
        print('JUVENIL')
    elif idade_nadador >14 and idade_nadador <=19:
        print('JUNIOR')
    elif idade_nadador > 19 and idade_nadador <= 20:
        print('SÊNIOR')
    else:
        print('MASTER')
'''
#42
'''
print('\033[36mÉ TRIÂNGULO? ESSE TRIÂNGULO É EQUILÁTERO, ESCALENO OU ISÓSCELES?\033[m')
a = int(input('Digíte o comprimento do 1º lado: '))
b = int(input('Digíte o comprimento do 2º lado: '))
c = int(input('Digíte o comprimento do 3º lado: '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('\033[1;31mNao pode formar triângulo.\033[m')
else:
    print('\033[1;34mpode formar triângulo.\033[m')
    if a == b and a == c:
        print('\033[1;34mEQUILÁTERO\033[m')
    elif a == b or a == c or b == c:
        print('\033[1;34mISÓSCELES\033[m')
    elif a != b and a != c and b != c:
        print('\033[1;34mESCALENO\033[m')
'''
#43 IMC
'''
print('\033[36mCÁLCULO DE IMC\033[m')
print('-' * 40)
peso = int(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura**2)
print(f'Seu IMC é de: {imc:.2f}.')
if imc < 18.5:
    print('\033[1;33mABAIXO DO PESO\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[1;34mPESO IDEAL\033[m')
elif imc > 25 and imc <=30:
    print('\033[1;33mSOBREPESO\033[m')
elif imc > 30 and imc <= 40:
    print('\033[1;33mOBESIDADE\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA\033[m') 
''' 
#44
'''
from time import sleep
valor_pago = float(input('Digíte o valor pago pelo produto: '))
forma_pagamento = input('Imforme a forma de pagamento: ').strip().lower()
print('AGUARDE...')
sleep(4)
if forma_pagamento == 'dinheiro' or forma_pagamento == 'cheque':
    print(f'Em dinheiro ou cheque, o valor saíra R${valor_pago - (valor_pago * 10) / 100:.2f} reais.')
elif forma_pagamento == 'a vista no cartão':
    print(f'A vista no cartão, sairá R${valor_pago - (valor_pago * 5) / 100:.2f} reais.')
elif forma_pagamento == '2x no cartão':
    print(f'Em 2x no cartão, sairá R${valor_pago / 2:.2f} reais')
elif forma_pagamento == '3x no cartão':
    print(f'Em 3x no cartão, sairá R${(valor_pago + (valor_pago * 20) / 100)/3:.2f} reais.')
else:
    print('\033[1;31mErrado, digíte novamente \033[m')
'''

#45
'''
print('\033[36mJOGO DO JOKEMPÔ\033[m')
print('-*' * 60)
import random
from time import sleep
choice = ['pedra','papel','tesoura']
escolha = input('Escolha "pedra", "papel" ou "tesoura": ').strip().lower()
print('AGUARDE...')
sleep(4)
if escolha not in choice:
    print('ERRO! DIGÍTE NOVAMENTE')
else:
    choice1 = random.choice(choice)
    print(f'Você escolheu: {escolha}.')
    print(f'IA escolheu: {choice1}.')
    if escolha == choice1:
        print('\033[33mEMPATE \033[m')
    elif escolha == 'pedra' and choice1 == 'tesoura' or escolha == 'tesoura' and choice1 == 'papel' or escolha == 'papel' and choice1 == 'pedra':
        print('\033[32mVOCÊ GANHOU\033[m')
    else:
        print('\033[31mVOCÊ PERDEU\033[m')
'''
