''' EXC 37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- Digitando 1 para binário.
- Digitando 2 para octal.
- Digitando 3 para hexadecimal. '''

numero = int(input('Digite qual o numero você quer conventer? Digite-o: '))

converter = int(input('''Qual a conversão desse número?\n- Digitando 1 para binário.
- Digitando 2 para octal.
- Digitando 3 para hexadecimal.
Conversão para: '''))

if converter == 1:
    res = bin(numero) # Função para Cálculo do Binário - bin()
    print(f'Resultado binário: {res}')
elif converter == 2:
    res = oct(numero) # Função para Cálculo do Octal - oct()
    print(f'Resultado em Octal: {res}')
elif converter == 3:
    res = hex(numero) # Função para Cálculo do Hexadecimal - hex()
    print(f'Base em Hexadecimal: {res}')
else:
    print('Número inválido para a operação')
