# Questão 1:
# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma 
# de A + B é menor que C, caso contrário, imprima que a A + B é maior que C.

import os
os.system("clear")

valor_A = int(input("Digite valor A: "))
valor_B = int(input("Digite valor B: "))
valor_C = int(input("Digite valor C: "))

if valor_A + valor_B < valor_C:
   print("É MENOR QUE C!")
else: 
    print("É MAIOR QUE C!")