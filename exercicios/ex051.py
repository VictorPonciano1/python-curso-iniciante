''' EXC 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão '''

n1 = int(input('Digite qual o primeiro termo da sua progressão: '))
n2 = int(input('Digite qual a razão da sua progressão: '))

termo10 = n1 + (10 - 1) * n2 # Forma de descobrir o 10º termo de uma O

for pa in range(n1, termo10, n2):
    print(pa, end=' >>> ')
print('\\\\')
