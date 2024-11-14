N = 1
notas = []
# funções ---------------------------------------------------------------
def med_arit(a):
    result = (a[0] + a[1] + a[2]) / 3
    return print(f"A média aritmética do aluno é: {result}")

def med_pond(a):
    # para média ponderada se multiplica as notas pelos pesos:
    a1 = a[0] * 5
    b1 = a[1] * 3
    c1 = a[2] * 2
    # depois soma as notas:
    somanota = a1 + b1 + c1
    # soma os pesos:
    somapesos = 5 + 3 + 2
    # e divide a soma das notas pela soma dos pesos
    medpond = somanota / somapesos
    return print(f"A média ponderada do aluno é: {medpond}")
# -----------------------------------------------------------------------


while N <= 3:
    nota = int(input(f"Digite a {N}ª nota do aluno: "))
    notas.append(nota)
    N += 1

letra = str(input("Digite qual média deverá ser usada no cálculo. \n(A) média aritmética \n(P) média ponderada\n\n-> ")).upper

if letra == "A":
    print(med_arit(notas))
if letra == "P":
    print(med_pond(notas))