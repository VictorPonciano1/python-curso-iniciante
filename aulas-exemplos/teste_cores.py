''' # Usado para testes # '''

# É POSSÍVEL DEFINIR OS ESTILOS POR MEIO DE VARIÁVEIS
# a = 3
# b = 43
# print(f'\033[{a};{b}m Texto\033[m')

# É POSSÍVEL CRIAR UM OBJETO CORES PARA ESCOLHER QUAL USAR
cores = {'limpo':'\033[0m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}

print('=' * 35)
print(f'{cores["vermelho"]}Exibindo todos os estilos possíveis{cores["limpo"]}')
print('=' * 35)

# Está exibindo em formato de sequência - primeiro exibe todos para então ir para o próximo
for style in [0, 1]: # Estilo 0: Padrão - 1: Negrito
    for text in range(30, 38):
        for back in range(40, 48):
            codigo = f'\033[{style};{text};{back}m'
            reset = '\033[0m'
            print(f'{codigo} Estilo{style} Texto{text} Fundo{back} {reset}', end=" ")
        print()
    print()
