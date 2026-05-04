''' EXC 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: MAGREZA;
- Entre 18.5 e 24.9: PESO IDEAL;
- Entre 25 e 29.9: SOBREPESO;
- Entre 30 e 39.9: OBESIDADE;
- Maior que 40: OBESIDADE MÓRBIDA; '''

altura = float(input('Digite a sua altura (em metros): '))
peso = float(input('Digite seu peso (em quilos): '))

imc = peso / (altura * altura)

print(f'Seu IMC é de: {imc}.')

bio = str(input('Qual seu sexo biológico?')).upper()

# IMPLEMENTAR DEPOIS DIFERENÇA ENTRE O IMC MASCULINO E O FEMININO
if bio == 'F' or bio == 'FEMININO':
    if imc < 18.5:
        print('MAGREZA')
    elif imc >= 18.5 and imc <= 25: 
        print('PESO IDEAL')
    elif imc >= 25 and imc < 30:
        print('SOBREPESO')
    elif imc >= 30 and imc < 40:
        print('OBESIDADE')
    else:
        print('OBESIDADE MÓRBIDA')
elif bio == 'M' or bio == 'MASCULINO':
    if imc < 19.5:
        print('MAGREZA')
    elif imc >= 19.5 and imc <= 25:
        print('PESO IDEAL')
    elif imc >= 25 and imc < 30:
        print('SOBREPESO')
    elif imc >= 30 and imc < 40:
        print('OBESIDADE')
    else:
        print('OBESIDADE MÓRBIDA')
else:
    print('Insira um sexo válido')
