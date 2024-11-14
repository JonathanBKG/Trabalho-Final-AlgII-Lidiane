N = 3 # variável global

def simetria (matriz):
    x = 0
    for l in range(N):
        for c in range(N):
            if(matriz[l][c] != matriz[c][l]):
                x = 1
    return x

mat = []

for l in range(N):
    aux = []
    for c in range(N):
        aux.append(int(input("Informe valores:")))
    mat.append(aux)

print(mat)
cont3 = simetria(mat)

if(cont3 == 1):
    print("A matriz não é simétrica!")
else:
    print("A matriz é simétrica!")