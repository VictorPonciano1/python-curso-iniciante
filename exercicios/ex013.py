# EXC 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Qual o  seu salário? Digite-o: R$'))

# Operações
promocao = salario * 0.15
salarioFinal = salario + promocao

# Outro jeito de fazer esse calculo
# promocao = salario + (salario * (15 / 100)) -> Neste caso a variável "salarioFinal" é desnecessária

cores = {'cls':'\033[0m',
         'blue':'\033[1;34m',
         'green':'\033[1;32m'}

print(f'{cores["blue"]}Valor do aumento (isolado): R${promocao:.2f}{cores["cls"]}')
print(f'{cores["green"]}Salário após o aumento de 15%: R${salarioFinal:.2f}{cores["cls"]}')
