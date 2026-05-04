''' EXC 65 - Crie um programa que leia vários números inteiros no teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não contnuar a digitar valores. '''

numeros = 0
soma = 0

digitados = 0
resposta = ''

maior = 0
menor = 0

while resposta in 'S':
    digitados = int(input('Digite um número: '))

    # Operações
    numeros += 1
    soma = soma + digitados

    # Maior e Menor
    if numeros == 1:
        maior = digitados
        menor = digitados
    else:
        if digitados > maior:
            maior = digitados
        if digitados < menor:
            menor = digitados

    # Verificação de Parada
    resposta = str(input('Deseja continuar? [S/N]: ')).upper()

media = soma / numeros

# Respostas Primárias
print(f'Total de Números Digitados: {numeros}')
print(f'Soma: {soma}')
print(f'Média: {media}')

# Verificação de Maior e Menor
print(f'O maior valor foi: {maior}')
print(f'O menor número foi: {menor}')
