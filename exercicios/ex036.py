''' EXC 36 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal (parcela) sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. '''

# Variáveis
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu Salário? R$'))
anos = int(input('Em quantos anos planeja pagá-la? '))

parcela = casa / (anos * 12) # Calculo da Parcela - Verificar quantos meses

print(f'O valor das suas parcelas em {anos} anos será de R${parcela:.2f}')

limite = salario * 0.30 # Ou salario * (30 / 100)

if parcela > limite:
    print('O valor da parcela supera 30% do seu salário - Empréstimo negado!')
else:
    print('O valor da parcela não supera o limite, o empréstimo está concedido!')
