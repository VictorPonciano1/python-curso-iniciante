''' Usado para testes '''

nome = str(input('Digite seu nome: ')).upper()

# Primeira vez fazendo as cores na mesma linha
cores = {'cls':'\033[0m','blue':'\033[1;34m','green':'\033[1;32m','red':'\033[1;31m'}

print(f'Olá {nome}!')

if nome == 'VICTOR':
    print(f'{cores["blue"]}Que nome bonito!{cores["cls"]}')
elif nome == 'FELIPE':
    print(f'{cores["green"]}Acho que já vi esse nome antes.{cores["cls"]}')
elif nome in 'NABUCODONOSSOR XERXES TUTANCAMON PALPATINE':
    print(f'{cores["red"]}Eita, temos um Imperador no sistema.{cores["cls"]}')
else:
    print('Seu nome não é especial no sistema.')
