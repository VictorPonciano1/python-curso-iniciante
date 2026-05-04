''' EXC 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é hora de se alistar;
- Se já passou do tempo do alistamento;
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

import datetime # Nota: nessa biblioteca, o mês vem antes do dia;

# Formatação de cores do Python
cores = {'cls':'\033[0m',
         'green':'\033[1;32m',
         'red':'\033[1;31m',
         'yellow':'\033[1;33m'}

agora = datetime.date.today().year # Pega apenas a informação do ano atual

print(f'Estamos no ano de {agora}')

nascimento = int(input('Digite em qual ano você nasceu: '))

idade = agora - nascimento
print(f'Você está com {idade} anos.')

bio = str(input('Qual o seu sexo biológico? Digite \"M\" para Masculino e \"F\" para feminino: ')).upper()

if bio == 'F':
    print('Você é mulher. Seu alistamento não é obrigatório.')
elif bio == 'M':
    print('Você é homem. Seu alistamento é obrigatório.')
    if idade == 18:
        print(f'{cores["yellow"]}Está no ano que você deve se alistar.{cores["cls"]}')
    elif idade < 18:
        diferenca = 18 - idade
        print(f'{cores["green"]}Ainda falta(m) {diferenca} ano(s) até que você precise se alistar{cores["cls"]}')
        print(f'Seu ano de alistamento será {agora + diferenca}')
    else:
        diferenca = idade - 18
        print(f'{cores["red"]}Você deveria ter se alistado a {diferenca} ano(s).{cores["cls"]}')
        print(f'Seu ano de alistamento foi {agora - diferenca}')
else:
    print(f'{cores["red"]}Digite um sexo biológico válido.{cores["cls"]}')
