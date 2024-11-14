matriz = []
soma = 0

for l in range(5):
    lista = []
    for c in range(5):
        lista.append(int(input(f"Informe o valor da posição: {l}, {c}: ")))
    matriz.append(lista)


print(matriz)
print("\n\nCalculadora dos valores da diagonal principal! ")

l = 0
c = 0

while l < len(matriz):
    c = 0
    while c < len(matriz[l]):
        if (l == c):
            soma += matriz[l][c]
        c += 1
    l += 1

print(soma)