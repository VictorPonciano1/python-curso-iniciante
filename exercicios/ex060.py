''' EXC 60 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5x4x3x2x1 = 120 '''

# Jeito 1 - Utilizando a Biblioteca Math (forma simplificada)

import math

print('1) Utilizando a Biblioteca Math e suas operações (forma simplificada).')

n1 = int(input('Digite um número: '))
f1 = math.factorial(n1)

print(f'O Fatorial de {n1}! é: {f1}')

# Espaçamento
print('='*40)

# Jeito 2 - Realizando da forma como o Exercício foi proposto
print('2) Utilizando o While, jeito original que o exercício foi proposto.')

n2 = int(input('Digite um número: '))
cont = n2
f2 = 1

print(f'Você escolheu o fatorial de {n2}!')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='') # É possível utilizar um "if" em um print
    f2 *= cont
    cont -= 1

print(f2)

# Espaçamento
print('='*40)

# Jeito 3 - Utilizando a estrutura de Repetição "For"
print('3) Utilizando estrutura "For".')

n3 = int(input('Digite um número: '))
cont2 = 1

print(f'Você quer o fatorial de {n3}!')

for n3 in range (n3, 0, -1):
    print(n3, end='')
    print(' x ' if n3 > 1 else ' = ', end='')
    cont2 *= n3

print(cont2)
