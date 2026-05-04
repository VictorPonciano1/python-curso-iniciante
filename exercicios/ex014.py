# EXC 14 - Escreva um programa que converta uma temperatura digitada em °C para °F (adicional: faça também para °K)

# 1- De Celsius para Fahrenheit - Vermelho
tempC = float(input('Digite a temperatura atual do seu local em °C: '))
tempF = (tempC * 1.8) + 32

# 2- De Celsius para Kevin - Azul
tempK = tempC + 273.15 # Valor de Graus Kevin é pré definido para 273.15

# 3- De Fahrenheit para Celsius - Verde
tempF2 = float(input('Digite qual a sua temperatura local em °F: '))
tempC2 = (tempF2 - 32) * 5/9

# Definição de cores
cores = {'cls':'\033[0m', # CLS: Clear Screen - Limpa a formatação
         'red':'\033[1;31m',
         'blue':'\033[1;34m',
         'green':'\033[1;32m'}

# Exibição dos Resultados
print(f'{cores["red"]}1- Valor em Celsius: {tempC:.1f}°C convertido em Fahrenheit: {tempF:.1f}°F{cores["cls"]}')
print(f'{cores["blue"]}2- Valor em Celsius: {tempC:.1f}°C convertido em Kevin: {tempK:.1f}°K{cores["cls"]}')
print(f'{cores["green"]}3- Valor em Fahrenheit: {tempF2:.1f}°F convertido em Celsius: {tempC2:.1f}{cores["cls"]}')
