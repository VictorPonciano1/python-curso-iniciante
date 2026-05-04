# EXC 10 - Crie um programa que leia quanto dinheiro uma pessoa possui na carteira e mostre quantos dólares ela pode comprar (cotação estabelecida de acordo com o valor do dia 30/04/2025)

dinheiro = float(input('Digite quanto dinheiro possui na carteira: R$'))

# Fazer a conversão
dolar = 5.66

# Variáveis para representar a resposta (não são extremamente necessárias)
cambio = dinheiro / dolar
cambioInteiro = dinheiro // dolar

# Exibição
print(f'Dólares que você pode comprar: USD ${cambio:.2f}')
print(f'Dólares inteiros (sem centavos): USD ${cambioInteiro}')

# Nota - Possível também fazer com outras moedas seguindo esses princípios
