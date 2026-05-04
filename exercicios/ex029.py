""" EXC 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mesnagem dizendo que ele foi multado. A multa vai custar R$7,00 para cada km acima do limite """

cores = {'limpatela': '\033[0m',
         'red':'\033[1;31m',
         'green':'\033[1;32m'}

vel = int(input('Digite a velocidade de seu carro no radar: '))

if vel > 80:
    multa = vel - 80
    print(f"{cores['red']}Você foi multado! O valor da multa é: R${multa * 7},00{cores['limpatela']}")
# Esse else é desnecessário (basta só exibir a multa - pelo menos na minha visão)
else:
    print(f'{cores["green"]}Estava dentro do limite. Lembre-se de dirigir com segurança!{cores["limpatela"]}')
