lista5 = []
lista10 = []
listaX = []

# Variáveis
i = 1

# Primeira lista com 5 elementos.
print('Digite 5 valores para a primeira lista.\n')
while i <= 5:
    n = int(input(f'Digite o {i}º valor: '))
    lista5.append(n)
    i += 1

i = 1
# Segunda lista com 10 elementos.
print('Agora digite 10 valores para a segunda lista.\n')
while i <= 10:
    n = int(input(f'Digite o {i}º valor: '))
    lista10.append(n)
    i += 1

# Percorrendo a lista para ver se encontra algum numero igual.
i = 0
while i < len(lista5): # Loop pra percorrer a primeira lista.
    ii = 0 # Índice para a segunda lista
    while ii < len(lista10):
        if lista5[i] == lista10[ii]: # Verifica se os elementos são iguais.
            if lista5[i] not in listaX: # Verifica se já está na lista.
                listaX.append(lista5[i]) # Adiciona na lista comum.
        ii += 1
    i += 1

print('listas: ')
print(lista5)
print(lista10)

print('Elementos em comum: ')
print(listaX)