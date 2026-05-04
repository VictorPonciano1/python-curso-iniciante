# EXC 8 - Escreve um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros (tente adicionar medidas extras)

# Distância em metros
distancia = float(input('Quantos metros '))

# Valor em Centímetros
cm = distancia * 100

# Valor em Milímetros
mm = distancia * 1000

# Valor em Quilômetros
km = distancia / 1000

# Valor em Decimetros
dm = distancia * 10

# Exibindo
print(f'Metros: {distancia}\nCentímetros: {cm}\nMilímetros: {mm}\nQuilômetros: {km}')
print(f'Decimetros: {dm}')
