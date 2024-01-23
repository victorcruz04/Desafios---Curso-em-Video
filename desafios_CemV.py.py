# 3 Somando dois numeros
'''
num_01 = float(input('Digíte um número: '))
num_02 = float(input('Digíte outro número: '))
sum = num_01 + num_02
print('A soma de {} e {} será de {}.'.format(num_01,num_02,sum))
'''
# 4 Dissecando uma Variável:
'''
var = input('Digíte algo: ')
print(f'O tipo primitivo é: {type(var)}')
print('É um alphanumérico?: ',var.isalnum())
print('É alfabeto?: ',var.isalpha())
print('É um decimal?: ',var.isdecimal())
print(' É maiúsculo?: ',var.isupper())
print('É miúsculo?:',var.islower())
print('está capitalizada?: ',var.istitle())
print('só tem espaços?: ',var.isspace())
'''
# 5 fazendo o sucessor e o antecessor de um número inteiro de um número:
'''
num_int = int(input('Digíte um número interio, por favor: '))
ante = num_int - 1
suce = num_int + 1
print(f'O numero {num_int} tem seu antecessor {ante} e sucessor {suce}.')
'''
# 6 fazendo o dobro, triplo e a raiz quadrada de um número: 
'''
num = float(input('Digíte um núemro: '))
dobro_num = num * 2 
triplo_num = num * 3
raizQ = num**(1/2)
print(f'O número {num} possui seu dobro {dobro_num}, seu triplo {triplo_num}\n e sua raiz quadrada {raizQ}')
'''
# 7 media de notas notas:
'''
nota_01 = float(input('Digíte sua primeira nota, por favor: ')) 
nota_02 = float(input('Digíte sua segunda nota, por favor: '))
media = (nota_01 + nota_02) / 2
print(f'A média de {nota_01} e {nota_02}, será {media}.')
'''
# metros convertido para centímetros e milímetros:
''' 
num_metro = float(input('Digíte o valor em metros: '))
convert_cent = num_metro * 100
convert_mili = convert_cent * 10
print(f'O valor {num_metro} convertido para cemtímetros será de {convert_cent}\ne milímetros será de {convert_mili}.')
'''
# fazendo tabuada:
'''
a = 0
num = int(input('Digíte um número: '))
for i in range (10):
     a += 1
     tabu = num * a
     print(f'{num} x {a} = {tabu} ')
'''
# convertendo real para dolar
'''
real = float(input('Qual é o valor que você possui?: '))
real_dolar = real * 4.96
print(f'Com R${real:.2f} você terá US${real_dolar:.2f} dolares\npara usufluir.')
'''
# calcular a área e quantidade de tinta
'''
altura = float(input('Digíte a altura da parede: '))
largura = float(input('Digíte a largura da parede: '))
area = altura * largura
Qtinta = area / 2
print(f'A área da altura {altura} e da largura {largura} será de {area} e a \nquantidade e tintas que será usada é de {Qtinta} litros ')
'''
# preço com 5% de desconto
'''
price = float(input('Digite o preço do produto: '))
newPrice = (price * 5)/100
print(f'O preço R${price:.2f} reais com 5% de desconto será de: R${price - newPrice:.2f} reais.')
'''
#salario com 15% de aumento
'''
sal = float(input('Digíte o salario do funcionário: '))
aumento_sal = (sal*15)/100
print(f'O salario R${sal:.2f} com 15% de desconto, será de: R${sal + aumento_sal:.2f}.')
'''