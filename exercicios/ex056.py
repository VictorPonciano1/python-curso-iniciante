''' EXC 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo;
- Qual o nome do HOMEM mais velho; 
- Quantas mulheres tem menos de 21 anos; '''

# Declaração das Variáveis
somaIdade = 0
maiorIddH = 0
homemVelho = ''
mulherMenor = 0

# For - Laço de Repetição
for p in range(1, 5):
    # Declaração das Variáveis
    nome = str(input(f'Digite o Nome da {p}ª Pessoa: '))
    idade = int(input(f'Digite a Idade da {p}ª Pessoa: '))
    sexo = str(input(f'Digite o sexo da {p}ª Pessoa [F/M]: ')).upper()
    somaIdade += idade
    # Verificador do Homem mais velho
    if p == 1 and sexo == 'M':
        maiorIddH = idade
        homemVelho = nome
    if sexo == 'M' and idade > maiorIddH:
        maiorIddH = idade
        homemVelho = nome
    # Verificação da Mulher com menos de 21
    if sexo == 'F' and idade < 21:
        mulherMenor += 1
media = somaIdade / 4
print('-=' * 20)
print(f'Média de Idade do grupo: {media} anos.')
print(f'O homem mais velho é {homemVelho} com {maiorIddH} anos.')
print(f'Número de mulher com menos de 21 anos: {mulherMenor}')
