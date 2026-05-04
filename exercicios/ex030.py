# EXC 30 - Crie um programa que leia um número inteiro e exiba se ele é PAR ou ÍMPAR

cores = {'cls':'\033[0m',
         'green':'\033[1;32m',
         'red':'\033[1;31m'}

n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'{cores["green"]}Número par{cores["cls"]}')
else:
    print(f'{cores["red"]}Número ímpar{cores["cls"]}')
