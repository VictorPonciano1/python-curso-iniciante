''' EXC 55 - Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos '''

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f'Digite os pesos do {p}º paciente: '))

    # Verifica se é a primeira ocorrência, caso for ele é válido para os dois valores
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

# Apresentação de resultados
print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')
