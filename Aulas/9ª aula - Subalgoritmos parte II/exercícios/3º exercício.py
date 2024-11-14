def soma_diagonal (matriz):
    soma = 0
    for l in range(len(matriz)):
        soma = soma + matriz[l][l]
    return soma

mat = []
cont = 0
N = 4
for l in range(N):
    aux = []
    for c in range(N):
        aux.append(cont)
        cont = cont + 1
    mat.append(aux)

print(mat)

print(f"A soma da diagonal principal é {soma_diagonal(mat)}")