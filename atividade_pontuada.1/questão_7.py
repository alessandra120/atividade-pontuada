import os
os.system("clear")

nome = input("Digite o nome do produto: ")
quantidade_adquirida = int(input("Digite a quantidade adquirida: "))
preco_unitario = int(input("Digite o preço unitário: "))

total = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
    desconto = total * 0.02 
    print("Desconto: de 2%")
elif quantidade_adquirida <= 10:
    desconto = total * 0.03
    print("Desconto: de 3%")  
else:
    desconto = total * 0.05
    print("Desconto: de 5%") 

total_a_pagar = total - desconto

print(f"R${desconto}")
print(f"Total a pagar: R$ {total}")