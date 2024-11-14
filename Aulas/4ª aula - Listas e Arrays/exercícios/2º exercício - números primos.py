# Definindo as Listas
lista = []
lista_indice = []
lista_primo = []

# Definindo as Variáveis
i = 0
n = 0

print('Calculadora de números primos.')
# Pergunta quais são os valores para colocar na lista
while i < 9:
    n = int(input(f'Digite qualquer número: '))
    lista.append(n)

    # if para saber se é numero primo.    
    if n < 2: # Números menores que 2 não são primos.
        i += 1
        continue
    
    else:
        eh_primo = True
        for x in range(2, int(n ** 0.5) + 1): # Verifica se o número tem algum divisor entre 2 e a raiz quadrada do número.
            if n % x == 0: # Se encontrar divisor, o num não é primo.
                eh_primo = False
                continue
    
        if eh_primo:
            lista_indice.append(i) # Salva o idíce onde o número primo está.
            lista_primo.append(n)  # Salva o número primo.
            
        i += 1
print(' ')
print(' ')
print('Lista de números digitados: ')
print(lista)
print(' ')
print('Lista de números primos e logo abaixo seus índices: ')
print(lista_primo)
print(lista_indice)
