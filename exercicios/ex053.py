''' EXC 53 - Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços '''

frase = str(input('Digite sua frase: ')).strip().upper()

palavras = frase.split()   # Divide a string em várias sub strings
juncao = ''.join(palavras) # Junta a string depois dos espaços

contrario = '' # Inicialmente vazio

# Percorre "ao contrário" imprimindo as letras no inverso
for palindromo in range(len(juncao) - 1, -1, -1):
    contrario += juncao[palindromo]
print(f'Frase original: {juncao} / Seu inverso: {contrario}')

if juncao == contrario:
    print('É palíndromo')
else:
    print('Não é palíndromo')
