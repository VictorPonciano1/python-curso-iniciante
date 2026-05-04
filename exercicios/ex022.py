''' EXC 22 - Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome de com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letras tem o primeiro nome; '''

nome = str(input('Digite seu nome completo: ')).strip()

cores = {'cls':'\033[0m',
         'red':'\033[1;31m',
         'blue':'\033[1;34m',
         'back':'\033[1;90;42m'} # Back = Background = Fundo da mensagem

print('Impressão de todas as operações:')
print(f'{cores["red"]}Nome com letras inteiramente maiúsculas: {nome.upper()}{cores["cls"]}')
print(f'{cores["blue"]}Nome inteiramente em minúsculas: {nome.lower()}{cores["cls"]}')
print(f'{cores["back"]}Total de letras (sem espaços): {len(nome)-nome.count(' ')}{cores["cls"]}')

lista = nome.split()

print(f'Letras do primeiro nome: {len(lista[0])}')
