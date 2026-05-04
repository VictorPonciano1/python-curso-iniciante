''' EXC 47 - Crie um programa que mostre na tela todos os números todosos números pares que estão no intervalo entre 1 a 50 anos '''

# Jeito 1
for pares in range(1, 51):
    if pares % 2 == 0:
        print(pares)

# Jeito 2
for pares2 in range(2,51, 2):
    print(pares2) # Por já começar no 2 ele irá fazer de 2 em 2
