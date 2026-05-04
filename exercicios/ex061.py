''' EXC 61 - Refaça o "EXERCÍCIO 51", lendo o primeiro termo e a razão de uma Progressão Aritmética (PA), mostrando os 10 primeiros termos da Progressão usando a estrutura "While". '''

p1 = int(input('Digite qual o Primeiro Termo: '))
ra = int(input('Digite qual a razão da sua PA: '))

c = 0

print('Os 10 Primeiros Termos da sua PA são:')
while c < 10:
    print(f'{p1} -> ', end='')
    p1 += ra
    c += 1

print('\\\\')
