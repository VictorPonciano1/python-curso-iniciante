# EXC 35 - Desenvolva um programa que leia o comprimento de três (3) retas e diga se elas podem formar um triângulo

reta1 = int(input('Digite o comprimento da reta 1: '))
reta2 = int(input('Digite o comprimento da reta 2: '))
reta3 = int(input('Digite o comprimento da reta 3: '))

cores = {'cls':'\033[0m',
         'green':'\033[1;32m',
         'red':'\033[1;31m'}

# Fazendo a verificação
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'{cores["green"]}Podemos ter triângulo{cores["cls"]}')
else:
    print(f'{cores["red"]}Impossível ter triângulo{cores["cls"]}')
