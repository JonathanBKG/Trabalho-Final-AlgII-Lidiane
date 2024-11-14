def imprime_intervalo(y):
    i = 1
    while i <= y:
        if(i % 2 == 1):
            print(i)
        i = i + 1

x = int(input("Informe um valor para X: "))
imprime_intervalo(x)