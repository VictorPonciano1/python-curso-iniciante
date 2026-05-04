''' EXC 57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

sexo = str(input('Digite o seu sexo [M/F - apenas as iniciais]: ')).strip().upper()[0]

while sexo not in "MmFf":
    sexo = str(input('Sexo inválido! Digite novamente: ')).strip().upper()[0]

print(f'Você registrou o sexo {sexo}')
