# Faça um algoritmo que lê uma matriz M 5x5 e mostrar os 
# valores digitados para a matriz M.

import numpy as np
N = 5

matriz = np.zeros((N,N))

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input(f"Digite o valor que está em:{l},{c}: \n"))

print("Matriz 5x5: \n", matriz)
