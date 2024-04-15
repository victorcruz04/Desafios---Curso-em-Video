# 3 Somando dois numeros
'''
num_01 = float(input('\033[33;40mDigíte um número: \033[m'))
num_02 = float(input('\033[33;40mDigíte outro número: \033[m'))
sum = num_01 + num_02
print('\033[34;41mA soma de {} e {} será de {}.\033[m'.format(num_01,num_02,sum))
'''
# 4 Dissecando uma Variável:
'''
var = input('Digíte algo: ')
print(f'O tipo primitivo é: {type(var)}')
print('É um alphanumérico?: ',var.isalnum())
print('É alfabeto?: ',var.isalpha())
print('É um decimal?: ',var.isdecimal())
print('É maiúsculo?: ',var.isupper())
print('É miúsculo?:',var.islower())
print('está capitalizada?: ',var.istitle())
print('só tem espaços?: ',var.isspace())
'''
# 5 fazendo o sucessor e o antecessor de um número inteiro de um número:
'''
num_int = int(input('\033[36mDigíte um número inteiro, por favor: \033[m'))
ante = num_int - 1
suce = num_int + 1
print(f'\033[1;36mO numero {num_int} tem seu antecessor {ante} e sucessor {suce}.\033[m')
'''
# 6 fazendo o dobro, triplo e a raiz quadrada de um número: 
'''
num = float(input('\033[4;35mDigíte um número: \033[m'))
dobro_num = num * 2 
triplo_num = num * 3
raizQ = num**(1/2)
print(f'\033[1;37;30mO número {num} possui seu dobro {dobro_num}, seu triplo {triplo_num}\n e sua raiz quadrada {raizQ}\033[m')
'''
# 7 media de notas notas:
'''
nota_01 = float(input('\033[1;34mDigíte sua primeira nota, por favor: \033[m')) 
nota_02 = float(input('\033[1;34mDigíte sua segunda nota, por favor: \033[m'))
media = (nota_01 + nota_02) / 2
print(f'\033[1;31mA média de {nota_01} e {nota_02}, será {media}.\033[m')
'''
# 8 metros convertido para centímetros e milímetros:
'''
num_metro = float(input('Digíte o valor em metros: '))
convert_cent = num_metro * 100
convert_mili = convert_cent * 10
print(f'\033[1;32mO valor {num_metro} convertido para cemtímetros será de {convert_cent}\ne milímetros será de {convert_mili}.\033[m')
'''
# 9 fazendo tabuada:
'''
a = 0
num = int(input('Digíte um número: '))
for i in range (10):
    a +=1
    tabu = num * a
    print(f'\033[33m{num}\033[m x \033[34m{a:2}\033[m = {tabu} ')
'''
# 10 convertendo real para dolar
'''
real = float(input('Qual é o valor que você possui?: '))
real_dolar = real / 4.96
print(f'\033[1;34mCom R${real:.2f} você terá US${real_dolar:.2f} dolares\npara usufluir.\033[m')
'''
# 11 calcular a área e quantidade de tinta
'''
altura = float(input('\033[4mDigíte a altura da parede: \033[m'))
largura = float(input('Digíte a largura da parede: '))
area = altura * largura
Qtinta = area / 2
print(f'\033[1;35mA área da altura {altura} e da largura {largura} será de {area} e a \nquantidade e tintas que será usada é de {Qtinta} litros \033[m')
'''
# 12 preço com 5% de desconto
'''
price = float(input('Digite o preço do produto: '))
newPrice = (price * 5)/100
print(f'\033[1;32mO preço R${price:.2f} reais com 5% de desconto será de: R${price - newPrice:.2f} reais.\033[m')
'''
# 13 salario com 15% de aumento
'''
sal = float(input('Digíte o salario do funcionário: '))
aumento_sal = (sal*15)/100
print(f'O salario R${sal:.2f} com 15% de desconto, será de: R${sal + aumento_sal:.2f}.')
''' # metros convertido para centímetros e milímetros(2.0)
'''
num_metro = float(input('Digíte o valor em metros: '))
convert_cent = num_metro * 100
convert_mili = num_metro * 1000
convert_km = num_metro / 1000
convert_hm = num_metro / 100
convert_dam = num_metro / 10
convert_dm = num_metro * 10

print(f'O valor {num_metro} em kilometros será de {convert_km} \nEm hectômetro será de {convert_hm} \nEm decâmetro será de {convert_dam}')
print(f'Em decímetro será de {convert_dm} \nEm centímetro será de {convert_cent} \nEm milímetro será de {convert_mili}')
'''
# preço com 5% de desconto (2.0)
'''
price = float(input('Digite o preço do produto: '))
newPrice = (price * 5)/100
fprice = (price *10)/100
print(f'O produto com preço de R${price:.2f} reais pagado a vista com 5% de desconto será de: R${price - newPrice:.2f} reais \nSe parcelado pagará {price + fprice} com 10 porcento de imposto.')
'''
# 14 convertendo celsius para fahreinheit
'''
cel = int(input('Dígíte a temperatura neste momento: '))
convert_fah = (cel * 9/5) + 32
print(f'A temperatura em celsius {cel:.1f}°C convertido para fahrenheit será de {convert_fah:.1f}°F')
'''
# 15 aluguel de carros
''' 
day = int(input('Quanos dias você esteve com o carro?: '))
km = int(input('Quantos km/h rodado?: '))
price1 = day * 60 
price2 = km * 0.15
print(f'O preço a se pagar pelo aluguel será de R${price1 + price2:.2f}.')
'''
# 16 parte inteira de um número real 
'''
import math
num_real = float(input('Digíte um valor real: '))
num_int = math.trunc(num_real)
print(f'A parte inteira de {num_real} é de {num_int}.')
'''
# 17 hipotenusa
'''
import math
comp_cOp = float(input('Digíte o comprimento do cateto oposto: '))
comp_cAd = float(input('Digíte o comprimento do cateto adjacente: '))
pit = math.sqrt(comp_cOp*comp_cOp + comp_cAd * comp_cAd)
print(pit)
'''
# 18 seno,cosseno e tangente
'''
import math
ang = float(input('Digíte o angulo do triangulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
coss = math.cos(rad)
tang = math.tan(rad)
print(f'O angulo {ang}\nEm seno será {sen}\nEm cosseno será {coss:.2f} \nEm tangente será {tang:.2f}')
'''
# 19 sortear nomes
'''
import random
nome01 = (input('Digíte o primeiro nome: '))
nome02 = (input('Digíte o segundo nome: '))
nome03 = (input('Digíte o terceiro nome: '))
nome04 = (input('Digíte o quarto nome: '))
lista = [nome01,nome02,nome03,nome04]
name_ch = random.choice(lista)
print(f'O nome escohido foi {name_ch}')
'''
# 20 ordenar quem vai apresentar
'''
import random
nome01 = (input('Digíte o primeiro nome: '))
nome02 = (input('Digíte o segundo nome: '))
nome03 = (input('Digíte o terceiro nome: '))
nome04 = (input('Digíte o quarto nome: '))
lista = [nome01,nome02,nome03,nome04]
random.shuffle(lista)
print(f'Na ordem será de {lista}')
'''
# 21 rodando mp3
'''
import pygame
pygame.init()
pygame.mixer.music.load('buscandote.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Digite espaço para pausar a música.')
pygame.mixer.pause()
'''
