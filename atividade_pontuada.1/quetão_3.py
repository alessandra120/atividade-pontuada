# Questão 3:
# Faça um algoritmo que leia dois valores inteiros A e B se os valores forem
# iguais deverá se somar os dois, caso contrário multiplique A por B. 
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para
# uma variável C e mostrar seu conteúdo na tela.

import os
os.system("clear")

valor_A = float(input("Digite valor_A: "))
valor_B = float(input("Digite valor_B: "))

if valor_A == valor_B:
    valor_C = (valor_A + valor_B)
else:
    valor_C = (valor_A * valor_B)

print(f"valor_C: {valor_C}")






