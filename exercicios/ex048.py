''' EXC 48 - Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500 '''

soma = 0
cont = 0

for imp in range(1, 501):
    if imp % 2 == 1 and imp % 3 == 0:
        soma += imp
        cont += 1
print(f'Soma de todos os {cont} números ímpares múltiplos de 3 é: {soma}')
