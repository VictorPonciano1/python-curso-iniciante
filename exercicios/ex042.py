''' EXC 42 - Refaça o DESAFIO 35 dos triângulos, acresdentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais; 
- Isóceles: dois lados iguais;
- Escaleno: todos os lados diferentes; '''

# Cálculo dos Lados
a = float(input('Lado 1 do Triângulo: '))
b = float(input('Lado 2 do Triângulo: '))
c = float(input('Lado 3 do Triângulo: '))

if a + b < c or a + c < b or b + c < a:
    print('Não pode ter Triãngulo.')
elif a == b == c:
    print('Triângulo Equilátero.')
elif a == b or b == c or c == a:
    print('Triângulo Isósceles.')
else:
    print('Triângulo Escaleno.')
