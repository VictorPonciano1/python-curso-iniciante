# Utilizado para testes

print(5 + 3 * 2) # 1- 3*2 = 6 ; 2- 5+6 = 11
print(3 * 5 + 4 ** 2) # 1- 4**2 = 16 ; 2- 3*5 = 15 ; 3- 15+16 = 31

n1 = int(input('digite um numero'))
n2 = int(input('digite outro numero'))

s = n1+n2 # Soma
p = n1*n2 # Produto
q = n1/n2 # Quociente
print('Soma = {} \nProduto = {}'.format(s, p), end=' >>> ') # Nova forma de exibir resultados
print('Quociente {}'.format(q))
