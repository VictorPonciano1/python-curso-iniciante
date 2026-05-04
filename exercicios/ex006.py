# EXC 6 - Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada

# Importante biblioteca externa
import math

number = int(input('Digite um número: '))

# Exibir o resultado diretamente sem criar outras variáveis "auxiliares" para isso
print(f'Seu dobro: {number*2}\nSeu triplo: {number*3}')

# Jeito 1 de fazer uma raiz quadrada
print(f'Sua raiz quadrada: {number**(1/2)}')

# Jeito 2 de fazer uma raiz quadrada
print(f'Sua raiz quadrada (jeito 2): {math.sqrt(number)}')

# Jeito 3 de fazer uma raiz quadrada
print(f'Sua raiz quadrada (jeito 3): {pow(number,(1/2))}')
