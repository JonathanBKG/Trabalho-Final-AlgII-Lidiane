matriz = []
listaC9 = []
listaL8 = []
N = 10

# Trocar os valores: 2 > 8   ||   5 > C9

# Preenchendo a matriz 10x10:
# for l in range(N):
#     lista = []
#     for c in range(N):
#         lista.append(int(input(f"Digite o valor da posição: {l}, {c}")))
#     matriz.append(lista)

matriz = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
[21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
[31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
[41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
[51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
[61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
[71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
[81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
[91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]

# zerando os índices.
c = 0
l = 0



# Copiando todos os valores da linha 8:
l = 8
for c in range(N):
    listaL8.append(int(matriz[l][c]))

# trocando os índices da linha 2 pelos da linha 8
matriz[2] = listaL8

# copiando todos os valores da coluna 9:
l = 0
c = 9
for l in range(N):
    listaC9.append(int(matriz[l][c]))
c = 0

matriz[5] = listaC9

print(matriz)