import os
os.system("clear")

valor_A = float(input("Digite valor_A: "))
valor_B = float(input("Digite valor_B: "))

if valor_A == valor_B:
    valor_C = (valor_A + valor_B)
else:
    valor_C = (valor_A * valor_B)

print(f"valor_C: {valor_C}")