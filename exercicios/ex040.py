''' EXC 40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO;
- Média entre 5.0 e 5.9: RECUPERAÇÃO;
- Média 7.0 ou superior: APROVADO; '''

cores = {'cls':'\033[0m',
         'green':'\033[1;32m',
         'red':'\033[1;31m',
         'yellow':'\033[1;33m'}

nota1 = float(input('Digite a primeira nota: '))  
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Nota final: {media}')

if media < 5.0:
    print(f'{cores["red"]}REPROVADO{cores["cls"]}')
elif media >= 5.0 and media < 6.0:
    print(f'{cores["yellow"]}RECUPERAÇÃO{cores["cls"]}')
else:
    print(f'{cores["green"]}APROVADO{cores["cls"]}')
