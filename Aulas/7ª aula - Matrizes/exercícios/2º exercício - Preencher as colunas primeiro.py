import numpy as np
N = 5

matriz = np.zeros((N,N))

for c in range(len(matriz)):
    for l in range(len(matriz[c])):
        matriz[l][c] = int(input("Informe valores para a matriz: "))

print(matriz)