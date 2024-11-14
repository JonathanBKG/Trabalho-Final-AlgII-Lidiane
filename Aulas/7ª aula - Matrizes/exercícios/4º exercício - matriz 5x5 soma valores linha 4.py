matriz = []
soma = 0

# preenchendo a matriz 5x5:
for l in range(5):
    lista = []
    for c in range(5):
        lista.append(int(input(f"Informe o valor da posição: {l}, {c}: ")))
    matriz.append(lista)

# zerando as guias.
l = 0
c = 0

# while para percorrer cada valor da matriz. 

while l < len(matriz):
    c = 0
    while c < len(matriz[l]):
        # E somar os valores da linha 4.
        if (l == 4):
            soma += matriz[l][c]    
        c += 1
    l += 1


print("O resultado da soma da linha 4 da matriz é:")
print(soma)