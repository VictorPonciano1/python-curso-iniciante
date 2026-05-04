''' EXC 59 - Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa 
Seu programa deverá realizar a operação solicitada em cada caso. '''

# Adição de Cores para incremento
cores = {'cls':'\033[0m',
         'green':'\033[1;32m',
         'red':'\033[1;31m',
         'blue':'\033[1;34m'}

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

r = 0 # Variável "Resultado" usada nas operações 1 e 2

n = 0 # Controlador das Operações

while n != 5:
    # Seleção de Operações
    n = int(input('''Digite qual operação você deseja realizar:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
Operação: '''))
    # Operação da Soma
    if n == 1:
        r = n1 + n2
        print(f'{cores["blue"]}A soma dos números: {r}{cores["cls"]}')
    # Operação da Multiplicação
    elif n == 2:
        r = n1 * n2
        print(f'{cores["blue"]}O produto dos números: {r}{cores["cls"]}')
    # Operação de pegar o Maior Número
    elif n == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n1 == n2:
            print('Os dois números são iguais')
        else:
            print(f'O maior número é {n2}')
    # Operação de adicionar Novos Números
    elif n == 4:
        n3 = int(input('Digite um novo número: '))
        n4 = int(input('Digite ou novo número: '))
        print(f'Os números antigos são: {n1} e {n2} | Os novos números são {n3} e {n4}')
    else:
        print(f'{cores["red"]}Digite uma operação válida.{cores["cls"]}')

print(f'{cores["green"]}Você encerrou as operações.{cores["cls"]}')
