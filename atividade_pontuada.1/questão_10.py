import os
os.system("clear")

preco_alcool = 3.79
preco_gasolina = 6.59

litros = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Escolha o tipo de combustível (A - Álcool | G - Gasolina): ").upper()

if tipo_combustivel == 'A':
    preco_unitario = preco_alcool
    if litros <= 25:
        desconto = 0.02
    elif litros > 25:
        desconto = 0.05  
    else:
        desconto = 0.00  
elif tipo_combustivel == 'G':
    preco_unitario = preco_gasolina
    if litros <= 25:
        desconto = 0.03
    elif litros > 25:
        desconto = 0.05  
    else:
        desconto = 0.00  
else:
    print("Tipo de combustível inválido!")
    preco_unitario = 0
    desconto = 0

if preco_unitario > 0:
    valor_sem_desconto = litros * preco_unitario
    valor_com_desconto = valor_sem_desconto * (1 - desconto)
    
print(f"Valor sem desconto: R$ {valor_sem_desconto:.2f}")
print(f"Desconto aplicado: R$ {valor_sem_desconto - valor_com_desconto:.2f}")
print(f"Valor total: R$ {valor_com_desconto:.2f}")