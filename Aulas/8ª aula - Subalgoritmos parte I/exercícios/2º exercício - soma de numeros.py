# Funções -----------------------------------------------------------
def somaN(a,b):
    # se o valor A for maior que o valor B (Ex: (10)|(1) )
    # o if está organizando para que o valor A seja o menor valor e que o valor B seja o maior. (Ex: (1)|(10) )
    if a > b:
        caminhao = b
        b = a
        a = caminhao

    # agora podemos iniciar o código:
    num = a
    total = num
    while num < b:
        num += 1
        total += num
    return print(f"O total da soma dos numeros inteiros existentes entre {a} e {b} é:\n\n{total}")

# -------------------------------------------------------------------

a = int(input("Digite o 1º número: "))
b = int(input("Agora digite o 2º número: "))

# verificação de numeros negativos.


print(somaN(a,b))