# EXC 32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto

import datetime

ano = int(input('Digite o ano de sua preferência (0 representa o ano atual): '))

cores = {'cls':'\033[0m'}

# Transforma o número "0" no ano atual
if ano == 0:
    ano = datetime.date.today().year

# Dica para ano bissexto: verificar se é divisível por 4 (se está no módulo de 4) ou se quando é múltiplo de 100 ele for múltiplo de 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é biessexto')

# Tentando calcular todos os bissextos até 2100 - Funcionou ✅

for anobis in range (2025, 2100):
    if anobis % 4 == 0:
        print(f'O ano {anobis} é bissexto')
