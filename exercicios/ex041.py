''' EXC 41 - A Confederação Nacional de Notação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 
- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JUNIOR;
- Até 20 anos: SÊNIOR;
- Acima: MASTER; '''

import datetime # Nota: nessa biblioteca, o mês vem antes do dia

agora = datetime.date.today().year

nascimento = int(input('Digite em qual ano você nasceu: '))

idade = agora - nascimento
print(f'Você tem {idade} anos.')

if idade < 10:
    print('Categoria Mirim.')
elif idade > 9 and idade < 15:
    print('Categoria Infantil.')
elif idade > 14 and idade < 20:
    print('Categoria Júnior.')
elif idade == 20:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')
