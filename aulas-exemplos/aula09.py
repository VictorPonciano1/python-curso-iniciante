# Utilizado para testes

# Para lembrar: um índice em Python começa sempre no 0

frase = '   curso de python  '

# Impressão da Frase do jeito "Fatiado"
print(frase[3:10])

# Análise e Transformação
print(len(frase))
print(frase.upper())
print(frase.strip())
frase = frase.replace('python', 'programacao')

# Transforma linhas diferentes em 1 único print
print("""Lorem ipsum dolor sit amet consectetur adipiscing elit.
      Quisque faucibus ex sapien vitae pellentesque sem placerat. 
      In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. 
      Pulvinar vivamus fringilla lacus nec metus bibendum egestas. 
      Iaculis massa nisl malesuada lacinia integer nunc posuere.""")

# Caso esteja presente retorna a posição, caso não vai retornar -1
print(frase.find('python'))

# Slipt: Divisão de Strings
frase2 = 'Lorem ipsum dolor sit amet'
print(frase2.split()) # O split transforma uma frase em várias palavras diferentes
vetor = frase2.split()
print(vetor[1][2])
