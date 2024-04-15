#pessoas = {'nome':'Victor','sexo':'masculino','idade': 20}
#print(pessoas['nome'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#for k,v in pessoas.items():
    #print(f'{k} = {v}')
'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for
e in brasil:
    for k,v in e.items():
        print(f'o campo {k} tem valor {v}')
'''
#90
'''
aluno = {}
aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input('MÉDIA: '))
print('-='*30)
if aluno['media'] >=7:
    aluno['situação'] = 'aprovado'
elif aluno['media'] < 7 and aluno['media'] > 5:
    aluno['situação'] = 'recuperacão'
else:
    aluno['situação'] = 'reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}.')
'''
#91 game with dados
'''
from random import randint
from time import sleep
from operator import itemgetter
game = {'player1': randint(1,6),
        'player2': randint(1,6),
        'player3': randint(1,6),
        'player4': randint(1,6)}
ranking = list()
print('drawn values')
print('-='*30)
for k,v in game.items():
    print(f'{k} took in {v}.')
    sleep(1)
ranking = sorted(game.items(), key = itemgetter(1),reverse=True)
print('==ranking players==')
print('-='*30)
for k,v in enumerate(ranking):
    print(f'{k+1}° place: {v[0]} com {v[1]}')
'''
#92
'''
from datetime import datetime
register = dict()
register['nome'] = str(input('name: '))
birthdayYear = int(input('birthday year:'))
register['age'] = datetime.now().year - birthdayYear
register['ctps'] = int(input('Work card(0 if not): '))
if register['ctps'] != 0:
    register['year of hire'] = int(input('year of hire: '))
    register['salary'] = float(input('Salary: '))
    register['retirement'] = register['age'] +((register['year of hire']+35) - datetime.now().year)
print('-='*30)

for k,v in register.items():
    print(f' -{k} has a value of: {v}')
'''
#93
'''
player = dict()
partidas = list()
totGol = 0
player['nome'] = str(input('NOME: '))
total = int(input(f'Quantas partidas {player['nome']} jogou? '))
for c in range(1,total+1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
player['gols'] = partidas[:]
player['total'] = sum(partidas)
print('-='*30)
print(player)
print('-='*30)
for k,v in player.items():
    print(f'O campo {k} tem valor de {v}.')
print('-='*30)
print(f'O jogador {player['nome']} jogou {len(player['gols'])} partidas.')
for i,v in enumerate(player['gols']):
    print(f'Na partida {i} fez {v} gols.')
print(f'foi um total de {player['total']} gols.')
'''
#94
pessoas = dict()
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo[m/f]: '))
    while True:
        if pessoas['sexo'] != 'MmFf':
            

        else:
            break