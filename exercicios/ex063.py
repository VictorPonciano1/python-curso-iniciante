''' EXC 63 - Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. 
Exemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 '''

n = int(input('Digite quantos elementos da Sequência de Fibonacci você quer ver: '))
n2 = 1

# Variáveis de Controle
f1 = 0
f2 = 1
f3 = 1

# Valor inicial do Fibonacci
print('0 -> ', end='')

# Resolução e desenvolvimento da Sequência
while n2 < n:
    print(f'{f3} -> ', end='')
    f3 = f1 + f2
    n2 += 1
    f1 = f2
    f2 = f3

print('\\\\')
