''' EXC 50 - Desenvolva um programa leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o '''

soma = 0
cont = 0

for sominha in range(0,6): # Dá pra nesse caso escolher entre 0-6 iu 1-7
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Foram informados {cont} números pares.\nSoma de todos os pares: {soma}')
