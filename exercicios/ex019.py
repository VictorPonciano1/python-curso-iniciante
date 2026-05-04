# EXC 19 - Um professor quer sortear seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome delas e escrevendo o escolhido

import random
from time import sleep

nome1 = input('Digite o primeiro aluno: ')
nome2 = input('Digite o sgeundo aluno: ')
nome3 = input('Digite o terceiro aluno: ')
nome4 = input('Digite o quarto aluno: ')

# Criada uma lista - Arrays serão vistos futuramente
lista = [nome1, nome2, nome3, nome4]

sorteio = random.choice(lista)

print('\033[1;31m===PROCESSANDO===\033[0m')
sleep(3) # Causa um "delay" proposital no código

print(f'\033[1;34mAluno escolhido: {sorteio}\033[0m')
