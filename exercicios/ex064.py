''' EXC 64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando a flag)'''

numeros = 0 # Quais números foram digitados
soma = 0    # Soma dos números digitados

digitos = 0 # Quais números serão digitados

while digitos < 999:
    digitos = int(input('Digite um número [números de 999 para cima param a operação]: '))
    # if: Desconsidera a "flag" de parada (o 999 não é considerado)
    if digitos < 999:
        numeros += 1
        soma = soma + digitos

print(f'Foram digitados {numeros} números e a soma de todos foi de {soma}')
