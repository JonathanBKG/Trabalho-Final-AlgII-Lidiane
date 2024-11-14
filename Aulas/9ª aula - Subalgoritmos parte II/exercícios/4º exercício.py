N = 10

def quantidade_ocorrencias (v, valor):
    cont = 0
    for l in range(len(v)):
        if(v[l] == valor):
            cont = cont + 1
    return cont

vet = []
cont = 0
for i in range(N):
    vet.append(cont)
    cont = cont + 1

print(vet)

valor = int(input("Informe um valor para ser buscado "))

print(f"O valor {valor} aparece {quantidade_ocorrencias(vet, valor)} vez(es).")