valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar

valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o salário? "))
anos_pagar = int(input("Pagar em quantos anos? "))

prestação = valor_casa // anos_pagar

if prestação > 0.30 * salario:
    print("Desaprovado")
elif prestação < 0.30 * salario:
    print('Aprovado')