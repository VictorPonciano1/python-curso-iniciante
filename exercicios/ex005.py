# EXC 5 - Faça um programa que leia um número inteiro e mostre seu sucessor e antecessor

number = int(input('Digite um número: '))

# Jeito 1 de imprimir os valores
print(f'Número digitado: {number}\nAntecessor: {number-1}\nSucessor: {number+1}')
# Espaçamento
print('')

# Jeito 2 de imprimir os valores - Declarando variáveis
antecessor = number-1
sucessor = number+1

print(f'Número: {number}\nAntecessor: {antecessor}\nSucessor: {sucessor}')
