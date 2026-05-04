''' EXC 49 - Refaça o "Exercício 009", monstrando tabuada de um número que o usuário escolher, só que agora utilizando o "laço for" '''

n = int(input('Você gostaria de ver a tabuada de qual número? '))

for tabuada in range(1, 11):
    print(f' [{n}] x {tabuada} = [{tabuada * n}]')
