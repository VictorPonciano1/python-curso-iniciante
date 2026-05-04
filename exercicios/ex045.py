''' EXC 45 - Crie um programa que faça o computador jogar Jokenpô com você.
NOTA DO DEV: O código acabou ficando grande pela estrutura e lógica que eu acebei desenvolvendo, existem maneiras mais fáceis de fazer esse código'''

import random

print('Olá! Eu sou o Supercomputador, dessa vez estou pronto para jogar Jokenpô!')

jogador = str(input('''Qual o seu movimento? Pedra, papel ou tesoura?'
Tente me vencer: ''')).lower()

pc = ['tesoura', 'papel', 'pedra']

sorteio = random.choice(pc)

if jogador == 'tesoura' and sorteio == 'tesoura':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('Tivemos um empate.')
elif jogador == 'tesoura' and sorteio == 'pedra':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('HAHAHA! EU VENCI!')
elif jogador == 'tesoura' and sorteio == 'papel':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('Você me venceu, parabéns.')
elif jogador == 'papel' and sorteio == 'papel':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('Parece que dessa vez nós empatamos.')
elif jogador == 'papel' and sorteio == 'tesoura':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('HAHAHA! EU SEMPRE SOUBE QUE SERIA VITORIOSO!')
elif jogador == 'papel' and sorteio == 'pedra':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('Essa não... você me venceu.')
elif jogador == 'pedra' and sorteio == 'pedra':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('Nós empatamos, desta vez.')
elif jogador == 'pedra' and sorteio == 'papel':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('A VITÓRIA É MINHA! HAHAHA!')
elif jogador == 'pedra' and sorteio == 'tesoura':
    print(f'Seu movimento foi \'{jogador}\' e o meu movimento foi \'{sorteio}\'')
    print('Não posso acreditar... você venceu, porém foi apenas desta vez!')
else:
    print('Faça um movimento válido!')
