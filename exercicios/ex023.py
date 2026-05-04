# EXC 23 - Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos seus dígitos
# Exemplo: 1890 - Milhar: 1 / Centena: 8 / Dezena: 9 / Unidade: 0 (matematicamente ou com Strings)

# Strings - Durante o Exemplo, não foi devidamente abordado

# num = str(input('Digite um número entre 0 e 9999: '))

# print('')

# Matematicamente

num2 = int(input('Digite outro número: '))

u = (num2 // 1) % 10
d = (num2 // 10) % 10
c = (num2 // 100) % 10
m = (num2 // 1000) % 10

print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')
