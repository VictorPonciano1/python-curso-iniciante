# EXC 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta cobre uma área de 2m²

# Variáveis
altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))

# Tamanho em m²
tamanho = altura * largura

# Total de litros necessários ao todo - 2m² = 1 Litro de tinta
tinta = tamanho / 2

# Exibindo resultado
print(f'Tamaho da sua parede: {tamanho}m²\nLitros necessários para a parede: {tinta}L')
