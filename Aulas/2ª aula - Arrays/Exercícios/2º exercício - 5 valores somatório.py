# Faça um algoritmo que lê 5 valores para 
# uma variável do tipo vetor e determine o somatório 
# de todos os valores armazenados no vetor.
import numpy as np

#Variável
soma = 0

#Define o tamanho do Array
N = 5

#Preenche o array com zeros (0)
x = np.zeros(N)

#Preenche o array com valores que o usuário preferir
for i in range(N):
    x [i] = int(input(f'Informe um valor para V {i}: '))
    
for elemento in x:
    soma += elemento

print(soma)