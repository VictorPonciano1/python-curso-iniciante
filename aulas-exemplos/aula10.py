# Usado para testes

nota1 = float(input('Qual sua nota 1? '))
nota2 = float(input('Qual sua nota 2? '))

media = (nota1 + nota2) / 2

# if (tempo <= 3):
#     print('Seu carro é novo')
# else:
#     print('Seu carro é mais antigo')

# Jeito diferentes de fazer a operação
# print('carro novo' if tempo <= 3 else 'carro velho')

if media >= 6 :
    print("Passou de ano")
else:
    print("Reprovado")

# Jeito novo
print('Aprovado' if media >= 6 else 'reprovado')
