# Faça um programa que preencha uma estrutura (lista, tupla ou conjunto) com 9
# números inteiros, calcule e mostre os números primos e suas respectivas
# posições na estrutura.

lista = []
lista_indice = []
lista_primo = []

i = 0
n = 0

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

print('\n\nLista de números digitados: \n')
print(lista)
print('\nLista de números primos e logo abaixo seus índices: ')
print(lista_primo)
print(lista_indice)