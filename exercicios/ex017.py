# EXC 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math

catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))

hip = (math.pow(catop, 2)) + (math.pow(catad, 2))
hip2 = math.hypot(catop, catad)

# Jeito 1
print(f'Valor (aproximado) da hipotenusa é: {math.sqrt(hip)}')

# Jeito 2
print(f'Valor (aproximado) da hipotenusa é: {hip2}')
