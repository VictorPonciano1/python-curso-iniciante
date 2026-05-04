# EXC 15 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado

dias = int(input('Por quantos dias o carro foi alugado? '))
distancia = float(input('Quantos km ele percorreu nesse período? '))

# Jeito 1
aluguel = dias * 60
valorKm = distancia * 0.15
total = aluguel + valorKm

# Jeito 2 - Fazer na mesma linha sem utilizar variáveis auxiliares
# total = (dias * 60) + (distancia * 0.15)

print(f'Tempo alugado: {dias} dias\nDistância percorrida: {distancia}km')
print(f'Valor pelo número de dias: R${aluguel:.2f} - Valor pelo número de km: R${valorKm:.2f}')
msg = f'Valor total: R${total:.2f}'

if total > 1000:
    print(f'\033[1;31m{msg}')
elif total <= 1000 and total > 500:
    print(f'\033[1;33m{msg}')
else:
    print(f'\033[1;32m{msg}')
