# EXC 4 - Faça um programa que leia algo digitado pelo usuário mostre na tela seu tipo primitivo e todas as informações possíveis sobre esse algo

algo = input('Digite algo: ')

tamanho = len(algo) # Função adicional

# Saída de Dados de formas diferentes para testes de funcionalidade
print(f'O tipo primitivo do que você digitou é {type(algo)}')
print(f'É numérico? {algo.isnumeric()}')
print(f'Tamanho desse algo digitado: {tamanho}')
print(f'É um valor alphabético (apenas caracteres)? {algo.isalpha}')
print(f'É alphanumérico? {algo.isalnum()}')
print('Está totalmente em Minúsculo?', algo.islower())
print('Está totalmente em Maiúsculo?', algo.isupper())
print('É um campo com somente \"espaços\"?', algo.isspace())
print('Está capitalizada?', algo.istitle())
