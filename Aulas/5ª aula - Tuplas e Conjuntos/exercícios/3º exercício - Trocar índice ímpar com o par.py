# Faça um algoritmo que lê estrutura (lista, tupla ou conjunto),
# K que comporte 20 elementos. Troque a seguir os elementos 
# de índice ímpar com os de índice par imediatamente seguinte
# mostre no final como ficou a estrutura K, com as alterações.
K = []
i = 0
Cont = 1
ipar = []
iimpar = []
result = []


print("Digite 20 valores: \n")
while i < 20:
    num = int(input(f"N{Cont}º: "))
    K.append(num)
    i += 1
    Cont += 1

i = 0

# Separar os valores dos indices impares e pares
while i < len(K):
    if i == 0:
        result.append(K[i])
        i += 1
    else: 
        if i % 2 == 0:
            ipar.append(K[i])
            i += 1
        else:
            iimpar.append(K[i])
            i += 1

i = 0
# Juntar e trocar de lugar
while Cont <= 10:
    if Cont < 10:
        result.append(ipar[i])
    result.append(iimpar[i])
    i += 1
    Cont += 1

print("Resultado do código: \n")
print(result)