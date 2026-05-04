# EXC 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
# Exemplo: Ana Maria Silva - Primeiro: Ana / Último: Silva

nome = str(input('Digite seu nome completo: '))

nomeCompleto = nome.split()

print(f'Primeiro nome: {nomeCompleto[0]}')
print(f'Último nome: {nomeCompleto[len(nomeCompleto)-1]}')
