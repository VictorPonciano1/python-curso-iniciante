''' Usado para testes '''

# Exemplo 1

contador = 0

while contador != 3:
    contador = contador + 1
    print(contador)
print('acabou')

# Exemplo 2

n = 1

while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

# Exemplo 3

r = 'S'

while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')

# Exemplo 4

n = 1
pares = 0
impares = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'Você encerrou a sequência e digitou {pares} números pares e {impares} números impares')
