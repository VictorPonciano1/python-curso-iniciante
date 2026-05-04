''' Usado para testes - NOTA: No Python é possível colocar um 3º Parâmetro para controle da forma que o laço é percorrido '''

print('Loop 1:')
# Caso uma mensagem for definida ela será impressa
# Caso no print se colocar o nome do loop, serão impressas suas posições
for loop in range(0,3): #Lembrando que ele ignora a última posição
    # Como no Python não se usa chaves ('{}') é preciso identar o código do jeito certo
    print(f'oi - {loop}')
    print('--')
print('FIM')

# Espaçamento
print(' ')

# No Python, basta adicionar um "-1" para que loop percorra os indíces de forma inversa
print('Loop 2:')
for loop2 in range(3, 0, -1):
    print(loop2)
print('FIM')

# Espaçamento
print(' ')

# Possível controlar a quantidade de casas percorridas adicionando um número na mesma posição do -1
print('Loop 3:')
for loop3 in range(0, 6, 2):
    print(loop3)
print('FIM')

# Espaçamento
print(' ')

# Controlar os parâmetros do Loop
i = int(input('Início do Loop 4: '))
f = int(input('Final do Loop 4: '))
n = int(input('Quantas posições ele percorre por vez: '))
for loop4 in range(i, f, n):
    print(loop4)
print('FIM')

# Espaçamento
print(' ')

# Fazer o Loop receber valores
s = 0
for loop5 in range(0,5):
    n = int(input('Digite um número: '))
    s += n
print(f'A soma de todos os números é {s}')
