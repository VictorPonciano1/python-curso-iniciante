# EXC 18 - Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = int(input('Digite um ângulo: '))

# Nota: para este tipo de operação, é necessário converter para radianos
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Ângulo = {angulo}°\nSeno = {seno}\nCosseno = {cosseno}\nTangente = {tangente}')
