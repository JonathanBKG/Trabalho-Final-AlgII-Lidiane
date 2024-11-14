# Ler uma estrutura (lista, tupla ou conjunto), R de 5 elementos,
# inteiros, contendo o resultado da LOTO. A seguir ler outra estrutura
# (lista, tupla ou conjunto), A de 10 elementos inteiros contendo 
# uma aposta. A seguir imprima quantos pontos fez o apostador.

gabarito = set()
aposta =   set()
i = 1

print("Digite o Gabarito da aposta: \n")

# Criando o gabarito:
while i <= 5:
    x = int(input(f"Digite o N{i}º: "))
    gabarito.add(x)
    i += 1
i = 1

# Pegando a aposta:

print("\nAgora, digite os valores da aposta: \n")

while i <= 10:
    x = int(input(f"Digite o N{i}º: "))
    aposta.add(x)
    i += 1

# Gerando a pontuação:

acerto = (gabarito & aposta)


print(f"\n Parabéns! Você acertou: {len(acerto)} números! =D\n")
print("Valores acertados:")
print(acerto)

