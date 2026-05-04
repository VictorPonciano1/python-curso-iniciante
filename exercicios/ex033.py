# EXC 33 - Faça um programa que leia 3 (três) números e mostre qual é o maior e qual o menor
# NOTA PESSOAL: Acho que todas as verificações poderiam ser feitas com um For

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Verificação primária: para caso existem números iguais
if n1 == n2 or n2 == n3 or n3 == n1:
    print('\033[1;31mExistem números iguais!\033[0m')
    exit()

# Verificação caso n1 > n2 e n3:
if n1 > n2 and n1 > n3:
    print(f'\033[1;32mMaior: {n1}')
    if n2 > n3:
        print(f'\033[1;32mDo meio: {n2}\nMenor: {n3}')
    else:
        print(f'\033[1;32mDo meio: {n3}\nMenor{n2}')

# Verificação caso n2 > n1 e n3
if n2 > n1 and n2 > n3:
    print(f'\033[1;32mMaior: {n2}')
    if n1 > n3:
        print(f'\033[1;32mDo meio: {n1}\nMenor: {n3}')
    else:
        print(f'\033[1;32mDo Meio: {n3}\nMenor: {n1}')

# Verificação caso n3 > n1 e n2
if n3 > n1 and n3 > n2:
    print(f'\033[1;32mMaior: {n3}')
    if n1 > n2:
        print(f'\033[1;32mDo meio: {n1}\nMenor: {n2}')
    else:
        print(f'\033[1;32mDo meio: {n2}\nMenor: {n1}')
