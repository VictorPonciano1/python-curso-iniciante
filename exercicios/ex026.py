''' EXC 26 - Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez; '''

frase = str(input('Digite uma frase: ')).lower().strip()

cores = {'0':'\033[0m', # Limpa Tela
         '1':'\033[1;35m', # Magenta
         '2':'\033[1;36m', # Ciano
         '3':'\033[1;33m'} # Amarelo

print(f'{cores["1"]}Quantas vezes a letra \'a\' aparece: {frase.count('a')} vezes{cores["0"]}')

# find "normal": - começa sua procura do lado esquerdo de forma padrão -->
print(f'{cores["2"]}Sua primeira aparição foi na posição: {frase.find('a')+1}{cores["0"]}')

# rfind: right find - começa a procura do lado direito <--
print(f'{cores["3"]}Sua última aparição foi na posição: {frase.rfind('a')+1}{cores["0"]}')
