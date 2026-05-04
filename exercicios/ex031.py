""" EXC 31 - Desenvolva um programa que pergunte a distância de uma viagem em quilômetros (km). Calcule o preço da passagem, cobrando R$0,50 por km em viagens de até 200km e R$0,45 para viagens mais longas. """

distancia = int(input('Qual a distãncia de sua viagem (em quilômetros)? '))

passagem = 0

# Jeito 1
# if (distancia <= 200):
#     passagem = distancia * 0.50
#     print(f'Distância da viagem: {distancia}km.\nValor total: R${passagem}')
# else:
#     passagem = distancia * 0.45
#     print(f'Distância da viagem: {distancia}km.\nValor total: R${passagem}')

# Jeito 2 - if simplificdo (operador ternário) - Cores adicionadas

print(f'\033[1;34mSua viagem tem a distância de {distancia}km')

passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'O preço da sua viagem é R${passagem:.2f}\033[0m')
