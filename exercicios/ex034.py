""" EXC 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumentpo. Para salários superiores R$1250,00 basta calcular um aumento de 10%. Para salários inferiores ou iguais, basta calcular um aumento de 15% """

cores = {'cls':'\033[0m',
         'blue':'\033[1;34m',
         'green':'\033[1,32m'}

salario = float(input('Digite seu salario: '))

if salario > 1250:
    aumento = salario * 0.10 # Também possível: (salario * 10) / 100
    salario += aumento
    print(f'{cores["blue"]}Valor do aumento: {aumento:.2f}\nSalário pós aumento de 10%: R${salario:.2f}{cores["cls"]}')
else:
    aumento = salario * 0.15 # Também possível: (salario * 15) /100
    salario += aumento
    print(f'{cores["green"]}Valor do aumento: {aumento:.2f}\nSalário pós aumento: R${salario:.2f}{cores["cls"]}')
