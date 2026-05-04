''' EXC 52 - Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo '''

cores = {'cls':'\033[0m', 'green':'\033[1;32m', 'red':'\033[1;31m'}

cont = 0 # Contador utilizado para verificação
print()
n = int(input('Digite um número (a partir de 2): '))

for primo in range(1, n + 1):
    if n % primo == 0:
        print(f'{cores["green"]}', end=' ')
        cont += 1
    else:
        print(f'{cores["red"]}', end=' ')
    print(f'{primo}', end=' ')

# Aparência
print('\033[1;37m -=- \033[0m', end='')

# Faz a verificação se é primo ou não
if cont > 2:
    print(f'{cores["red"]}{n} não é um número primo.{cores["cls"]}')
else:
    print(f'{cores["green"]}{n} é um número primo.{cores["cls"]}')
