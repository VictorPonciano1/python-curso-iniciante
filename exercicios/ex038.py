''' EXC 38 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é MAIOR
- O segundo valor é MAIOR
- Não existe valor maior, os dois são IGUAIS '''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro numéro é maior')
elif n2 > n1:
    print('O segundo número é maior.')
else:
    print('São números iguais')
