import os
os.system("clear")

cor_cd = input("Digite a cor do CD: ")

match cor_cd:
    case "Verde" | "verde":
        print("Preço: R$ 10,00")
    case "Azul" | "verde":
        print("Preço: R$ 20,00")
    case "Amarelo" | "amarelo":
        print("Preço: R$ 30,00")
    case "Vermelho" | "vermelho":
        print("Preço: R$ 40,00")