''' EXC 46 - Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifícion indo de 10 até 0, com uma "pausa" de 1 segundo entre eles '''

import time

fogos = str(input('Você quer ver os fogos? Digite \"Sim\" ou \"Não\": ')).lower()

if fogos == 'sim':
    print('Atenção para contagem:')
    for articio in range(10, -1, -1):
        print(articio)
        time.sleep(1)
    print('\033[1;31mKABOOM\033[0m')
elif fogos == 'não' or fogos == 'nao':
    print('Os fogos não serão estourados')
else:
    print('Digite uma opção válida')
