gabarito = []
aposta   = []
lista_acertos = []


# Variáveis
i = 1

# Definir qual o gabarito da aposta.
print('Quais os números do gabarito da aposta?')
# Gabarito
while i <= 5:
    n = int(input(f'{i}º valor: '))
    gabarito.append(n)
    i += 1
# Pergunta para o usuário qual os números da aposta dele.
i = 1
print('Agora quais são os numeros apostados?')
while i <= 10:
    n = int(input(f'{i}º valor: '))
    aposta.append(n)
    i += 1

# Percorrendo a lista para ver se encontra algum numero igual.
i = 0
while i < len(gabarito): # Loop pra percorrer a primeira lista.
    ii = 0 # Índice para a segunda lista
    while ii < len(aposta):
        if gabarito[i] == aposta[ii]: # Verifica se os elementos são iguais.
            if gabarito[i] not in lista_acertos: # Verifica se já está na lista.
                lista_acertos.append(gabarito[i]) # Adiciona na lista comum.
        ii += 1
    i += 1

# agora contabilizando quantos números acertados.
print(f'Sua pontuação é de: {len(lista_acertos)} pontos!')
