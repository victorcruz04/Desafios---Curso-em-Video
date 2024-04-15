
'''
#lanche = 'Hamburguer','suco','pizza','pudin'
#print(sorted(lanche))
#for comida in lanche:
    #print(f'Eu vou comer {comida}.')
#print('Comi muito')
#for cont in range(0,len(lanche)):
    #print('eu vou comer', lanche[cont],'na posição',[cont])
#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posição {pos}.')
'''
# 72 numero por extenso
'''
numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','desessete','dezoito','dezenove','vinte')
while True:
    num =int(input('Digíte um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digítou o número {numeros[num]}.')
    else:
        print('inválido')
    dilema = input('Quer continuar?[S/N]').strip().lower()
    if dilema == 's':
        continue
    elif dilema == 'n':
        break
'''
#73 brasileirão
'''
brasileirão = ('Palmeiras','Grêmio','Atlético-MG','Flamengo',
                'Botafogo','Bragantino','Fluminense','Athletico-PR',
                'Internacional','Fortaleza','São Paulo','Cuiabá',
                'Corinthians','Cruzeiro','Vasco','Bahia','Santos',
                'Goiás','Coritiba','América-MG')
print(f'Os 5 primeiros são {brasileirão[0:5]}.')
print(f'O 4 últimos são {brasileirão[-4:]}.')
print(f'Os times em ordem alfabética são {sorted(brasileirão)}.')
print(f'o Corinthians está na {brasileirão.index('Corinthians')} posição.')
'''
#74 
'''
from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),
        randint(0,10),randint(0,10))
print(tupla)
print(f'\nO maior é {max(tupla)}.')
print(f'O menor número é {min(tupla)}.')
'''
#75
'''
tupla1 = (int(input('digíte um número: ')),
        int(input('digíte um número: ')),
        int(input('digíte um número: ')),
        int(input('digíte um número: ')),)
print(tupla1)
print(f'Apareceu a letra 9 {tupla1.count(9)} vezes .')
if 3 in tupla1:
    print(f'Apareceu na {tupla1.index(3)}º posição o primeiro valor 3')
else:
    print('O valor 3 não foi digitado.')
print('Os valores digitados foi,',end=' ')
for n in tupla1:
    if n %2 == 0:
        print(n,end=' ')
'''
#76
'''
print('-' * 40)
print(' ' * 10,'PREÇO DE PRODUTOS')
print('-' * 40)
listagem = ('GTA 6',500,
            'XBOX SERIES S', 3000,
            'TELEVISÃO 8K',4000,
            'CONTROLE ED/ LIMITADA',500,
            'CADEIRA', 1200)
for pos in range (0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end=' ')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-' * 40)
'''
#77
'''
palavras = ('Victor','Hugo','Almeida','Cruz')
vogais = 'AaEeIiOoUu'
for palavra in palavras:
    print(f'\nNa palavra {palavra}, temos',end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra,end=' ')
'''