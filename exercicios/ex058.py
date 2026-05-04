''' EXC 58 - Melhore o jogo do "EXERCÍCIO 28" onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''

# Importa a biblioteca random para "randomizar" números
import random

# Cores para incremento do código
cores = {'cls':'\033[0m',
         'green':'\033[1;32m',
         'red':'\033[1;31m'}

print('Eu, o SUPER COMPUTADOR, pensei em um número entre 0 e 10!')

pc = random.randint(0, 10)

n = 11      # Apenas um valor inicial para que seja possível o jogo
palpite = 0 # Número total de palpites do jogo

# Verificação (Execução do Jogo)
while n != pc:
    n = int(input('Em qual número eu estava pensando? Digite-o e teste sua sorte: '))
    palpite += 1
    if n != pc:
        print(f'{cores["red"]}Eu venci, tente novamente{cores["cls"]}')

print(f'{cores["green"]}Você me venceu e precisou de {palpite} chances para me vencer')
