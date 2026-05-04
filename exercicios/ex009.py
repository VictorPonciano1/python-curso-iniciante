# EXC 9 - Faça um programa que leia um número inteiro qualquer e imprima sua tabuada

n = int(input('Digite um número: '))

# Jeito 1 de fazer
print(f'Tabuada do [{n}]')
print('-' * 15)
print(f'[{n}] x  1 = {n*1}\n[{n}] x  2 = {n*2}\n[{n}] x  3 = {n*3}')
print(f'[{n}] x  4 = {n*4}\n[{n}] x  5 = {n*5}\n[{n}] x  6 = {n*6}')
print(f'[{n}] x  7 = {n*7}\n[{n}] x  8 = {n*8}\n[{n}] x  9 = {n*9}')
print(f'[{n}] x 10 = {n*10}')
print('-' * 15)

# Jeito 2 que eu pensei - Basicamente só está ocupando espaço como um comentário
# tb1 = n*1
# tb2 = n*2
# tb3 = n*3
# tb4 = n*4
# tb5 = n*5
# tb6 = n*6
# tb7 = n*7
# tb8 = n*8
# tb9 = n*9
# tb10 = n*10
# print('[{:1}] x 1 = {}\n[{:1}] x 2 = {}\n[{:1}] x 3 = {}'.format(n, tb1, n, tb2), n, tb3))
# print('[{:1}] x 4 = {}\n[{:1}] x 5 = {}\n[{:1}] x 6 = {}'.format(n, tb4, n, tb5, n, tb6))
# print('[{:1}] x 7 = {}\n[{:1}] x 8 = {}\n[{:1}] x 9 = {}'.format(n, tb7, n, tb8, n, tb9))
# print('[{:1}] x 10 = {}'.format(n, tb10))

# Nota - Também existem um jeito 3 de fazer onde cada resultado possui seu próprio print para ficar mais organizado
