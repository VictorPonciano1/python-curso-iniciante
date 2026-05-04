#Utilizado para testes

from math import sqrt, floor
import random

n = int(input('digite um numero: '))
raiz = sqrt(n) # Calculo da Raiz

# floor = chão : arredonda "para baixo" / ceil = teto : arredonda "para cima"
print('raiz de {} = {}'.format(n, floor(raiz)))

num = random.random() # Valores aleatórios entre 0 e 1 (decimais também)
num2 = random.randint(1, 10) # Valores aleatórios e inteiros (definidos entre 1 e 10)

print(num)
print(num2)
