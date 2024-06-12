soma = 0

while True:
    numero = float(input('Escreva um nuemro (0 para sair): '))

    if numero == 0:
        break
    elif numero > 0:
        soma = soma + numero

    print(soma)