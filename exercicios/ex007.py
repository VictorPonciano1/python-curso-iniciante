# EXC 7 - Desenvolve um programa que leia as duas notas de um aluno, então calcule e mostre sua média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

# Imprimindo com 1 casa decimal já trabalhando com as regras de arredondamento
print(f'Notas no aluno: {nota1:.1f} e {nota2:.1f}')
res = f'Média do aluno: {media:.1f}'

if media >= 6:
    print(f'\033[1;34m{res}\033[0m') # Imprime Azul
else:
    print(f'\033[1;31m{res}\033[0m') # Imprime Vermelho