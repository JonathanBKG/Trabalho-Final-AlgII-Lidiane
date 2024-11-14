# Ler 2 duas estruturas (lista, tupla ou conjunto), denominada R de 
# 5 elementos e S de 10 elementos, ambos de inteiros. Gere outra 
# estrutura X que possua os elementos comuns a R e a S. Considere 
# que na mesma estrutura não haverá números repetidos.

ConjA = set()
ConjB = set()

i = 1

print("Valores em comum!\n")
print("Digite 5 valores para o Grupo A: ")
while i <= 5:
    num = int(input(f"Valor N{i}º: "))
    ConjA.add(num)
    i += 1

i = 1

print("Certo, agora digite 10 valores para o Grupo B: ")
while i <= 10:
    num = int(input(f"Valor N{i}º: "))
    ConjB.add(num)
    i += 1

print("\nOs valores iguais são:")
print(ConjA & ConjB)