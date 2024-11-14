matriz = []
somaC = 0
somaDP = 0

# preenchendo a matriz 10x10:
for l in range(10):
    lista = []
    for c in range(10):
        lista.append(int(input(f"Informe o valor da posição: {l}, {c}: ")))
    matriz.append(lista)

# zerando as guias.
l = 0
c = 0

# while para percorrer cada valor da matriz. 

while l < len(matriz):
    c = 0
    while c < len(matriz[l]):
        # E somar os valores da coluna 2.
        if (c == 2):
            somaC += matriz[l][c]

        if (l == c):
            somaDP += matriz[l][c]    
        c += 1
    l += 1

print(f"Somatório dos valores da coluna 2 = {somaC}")
print(" ")
print(f"Somatório dos valores da diagonal principal = {somaDP}")