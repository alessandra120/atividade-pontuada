import os
os.system("clear")

valor_A = int(input("Digite o valor de A: "))
operador = input("Digite a operação que deseja: ")
valor_B = int(input("Digite o valor de B: "))

match operador:
    case "+":
        resultado = valor_A + valor_B
    case "-":
        resultado = valor_A - valor_B
    case "*":
        resultado = valor_A * valor_B

print(f"Resultado: {resultado}")