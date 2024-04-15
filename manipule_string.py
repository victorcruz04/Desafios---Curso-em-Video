#22 manupulando string
'''
num = str(input('Digíte seu nome completo: '))
num_1 = num.split()
print(f'Seu nome completo: {num}')
print(f'Seu nome em maiúsculo: {num.upper()}.')
print(f'Seu nome em minúsculo: {num.lower()}.')
print(f'Seu nome tem ao todo {len(num) - num.count(' ')} letras.')
print(f'{len(num_1[0])} letras no primeiro nome.')
'''
# 23 unidade, dezena, centena, milhar
'''
num = int(input('Digíte um número: '))
u = num // 1 % 10
d =  num // 10 % 10
c =  num //100 % 10
m = num //1000 % 100
print(f'Analizando: {num}.')
print(f'unidade: {u}')
print(f'Dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')
'''
# 24 true or false
'''
name_city = input('Digíte o nome de uma cidade: ').strip()
name_div = name_city.split()
div = name_div[0].upper()
a = 'SANTO' in div
print(a)
'''
#25 silva false or true
'''
name_a = input('Digite um nome: ').strip()
nam_up = name_a.upper()
name_b = nam_up.split()
a = 'SILVA' in name_b
print(a)
'''
# 26 encontrando uma letra da frase
'''
nam = str(input('Qual é seu nome?: ')).strip()
print(nam)
letter_R = nam.lower().count('a')
pos_R = nam.find('a')
ult_R = nam.rfind('a') 
print(f'Nome: {nam}, tem {letter_R} A, se encontra iniciamente na {pos_R + 1} posição \nE termina na {ult_R + 1} posição.')
'''
# 27 primeiro e último nome de uma pessoa
'''
nam_complete = input('Digíte seu nome completo: ').strip()
div = nam_complete.split()
prim = div[0]
ult = div[-1]
print('primeiro nome: ',prim)
print('ultimo nome: ',ult)
'''