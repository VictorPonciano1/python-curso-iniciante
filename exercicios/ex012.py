# EXC 12 - Faça o algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto

produto = input('Digite qual o produto: ')
preco = float(input('Digite qual seu preço: '))

# Jeito 1
desconto = preco - ((preco * 5) / 100)

# Jeito 2
# desconto = preco - (preco * 0.05) -> Porcentagem = n / 100

# Exibição
print(f'Produto: {produto}\nPreço Original: {preco:.2f}')
print(f'Preço com Desconto de 5%: {desconto:.2f}')
