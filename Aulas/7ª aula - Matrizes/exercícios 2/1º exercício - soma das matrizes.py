matriz1 = []
matriz2 = []
matrizR = []
soma = 0
N = 3

# perguntando ao usuário qual o tamanho da matriz:
N = int(input("Qual o tamanho da matriz quadrada?: "))

# preenchendo a 1ª matriz 5x5:
print("Preencha a 1ª matriz:\n")
for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input(f"Informe o valor da posição: {l}, {c}: ")))
    matriz1.append(lista)

l = 0
c = 0

# preenchendo a 2ª matriz 5x5:
print("Agora, preencha a 2ª matriz:\n")
for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input(f"Informe o valor da posição: {l}, {c}: ")))
    matriz2.append(lista)

l = 0
c = 0

# Somando as duas matrizes:
while l < len(matriz1):
    c = 0
    lista = []
    while c < len(matriz1):
        soma = matriz1[l][c] + matriz2[l][c]
        lista.append(soma)
        c += 1
    matrizR.append(lista)
    l += 1      

print("A matriz resultado é: \n")

for l in range(len(matrizR)):
    print(matrizR[l])