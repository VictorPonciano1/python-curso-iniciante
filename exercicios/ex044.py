''' EXC 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- À vista pix: 10% de desconto;
- À vista no cartão: 5% de desconto;  
- Em até 2x no cartão: preço normal;
- Em 3x ou mais no cartão: 20% de juros; '''

cores = {'cls':'\033[0m',
         'green':'\033[1;32m',
         'red':'\033[1;31m'}

# Produto comprado
produto = str(input('Digite o produto que será comprado: '))
# Preço do produto
preco = float(input('Digite qual o preço: R$'))
# Condicao de Pagamento
condicao = int(input('''Qual o método de pagamento?
                     1 = Pix;
                     2 = Cartão à vista;
                     3 = Cartão parcelado em 2x;
                     4 = Cartao3;
                     Digite o número correspondente: '''))

print(f'O produto que você vai comprar é {produto} e vai pagar com {condicao}')
print(f'O preço original R${preco}')

if condicao == 1:
    desconto = preco * 0.10
    preco = preco - desconto
    print(f'{cores["green"]}O pagamento com pix à vista te dá 10% de desconto. O preço final é: R${preco}{cores["cls"]}')
elif condicao == 2:
    desconto = preco * 0.05
    preco = preco - desconto
    print(f'{cores["green"]}O pagamento com cartão à vista te dá 5% de desconto: O preço final é: R${preco}{cores["cls"]}')
elif condicao == 3:
    print(f'{cores["green"]}O pagamento com parcelamento em 2x no cartão não te dá desconto. O preço final é: R${preco}{cores["cls"]}')
elif condicao == 4:
    juros = preco * 0.20
    preco = preco + juros
    print(f'{cores["green"]}O pagamento com cartão parcelado em 3 te dá 20% de juros no preço final. O valor final seria: R${preco}{cores["cls"]}')
else:
    print(f'{cores["red"]}Digite uma opção de pagamento válida.{cores["cls"]}')
