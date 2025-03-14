import os
os.system("clear")

kg_de_morangos = float(input("Digite quantidade de morangos foram comprados (em Kg): "))
kg_de_macas = float(input("Digite quantos de maçãs foram comprados (em Kg): "))

   
if kg_de_morangos <= 5:
    preco_morango = kg_de_morangos * 2.50
else:
    preco_morango = kg_de_morangos * 2.20
  
if kg_de_macas <= 5:
    preco_maca = kg_de_macas * 1.80
else:
    preco_maca = kg_de_macas * 1.50
   
valor_total = preco_morango + preco_maca
   
if kg_de_morangos + kg_de_macas >= 10 or valor_total > 15.00:
    desconto = valor_total * 0.10
    valor_total_com_desconto = valor_total - desconto
    print(f"Desconto de 10% aplicado: R$ {desconto:.2f}")
    print(f"Valor total a pagar com desconto: R$ {valor_total_com_desconto:.2f}")
else:
        print(f"Valor total a pagar: R$ {valor_total:.2f}")