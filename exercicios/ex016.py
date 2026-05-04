# EXC 16 - Crie um programa que leia um número Real (decimal) qualquer pelo teclado e mostra na tela sua porção inteira
# Exemplo: O número 6.823 tem a parte inteira 6

import math

n = float(input('Digite um número real (decimal): '))

# Jeito 1 - Floor (arredonda) 
print(f'A parte de inteira de {n} é {math.floor(n)}')

# Jeito 2 - Trunc (corta a parte inteira do número)
print(f'A parte inteira de {n} é {math.trunc(n)}')

# Jeito 3 - Sem importar módulos
print(f'A parte inteira do número {n} é {int(n)}')
