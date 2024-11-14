# 1º exercício:
# Escreva uma função que receba 2 números e retorne o maior
def maximo(a,b):
    if a > b:
        return a
    else:
        return b
    
# 2º exercício:
# Escreva uma função que receba 1 número e retorne TRUE se
# o numero for PAR
def epar(a):
    if a % 2 == 0:
        return "TRUE"
    else:
        return "FALSE"
    
# 3º exercício:
# Escreva uma função que receba o lado de um quadrado e
# retorne a sua área (A = lado²)
def area_quadrado(a):
    b = a * a
    return b

# 4º exercício:
# Escreva uma função que receba a base e a altura de um
# triângulo e retorne sua área (A = (base x altura) /2).
def area_triangulo(Base,Altura):
    c = (Base * Altura) / 2
    return c