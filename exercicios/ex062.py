''' EXC 62 - Melhore o "EXERCÍCIO 61", perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar "0 TERMOS". '''

# A Base do código é a mesma do "EXERCÍCIO 61", porém sofreu alterações

p1 = int(input('Digite qual o Primeiro Termo: '))
ra = int(input('Digite qual a razão da sua PA: '))

c = 0
limite = 0
extra = 10 # Controle inicial do código

print('Os 10 Primeiros Termos da sua PA são:')
while extra != 0:
    limite = limite + extra
    while c < limite:
        print(f'{p1} -> ', end='')
        p1 += ra
        c += 1
    print('PAUSA')
    extra = int(input('Deseja ver quantos termos extra? Digite: '))

print('='*50)
print('FIM DA EXECUÇÃO')
print(f'Foram exibidos ao todo {limite} termos.')
