''' EXC 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores '''

import datetime

agora = datetime.date.today().year

contMaior = 0 # Contador Maiores de Idade
contMenor = 0 # Contador Menores de Idade

for verificador in range (1,8):
    n = int(input(f'Digite o ano em que a pessoa nº{verificador} nasceu: '))
    idade = agora - n
    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1

print(f'Número de maiores de idade: {contMaior}')
print(f'Número de menores de idade: {contMenor}')
