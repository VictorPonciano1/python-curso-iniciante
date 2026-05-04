# EXC 25 - Crie um programa que que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Digite um nome: ')

# in: não é método, é um operador do Python (bem útil)
print(f'O nome possui Silva? {'silva' in nome.upper()}')
