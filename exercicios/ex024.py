# EXC 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome = str(input('Digite o nome de uma cidade (que tenha nome composto) ')).strip()

# O enunciado diz: apenas se COMEÇAR com "Santo"
print(f'Começa com \'Santo\'? {nome[:5].lower() == 'santo'}')
