import os
os.system("clear")

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

print(f"Média: {media}")

if media >= 6.0:
    situação = "Parabéns!"
elif media >= 4.0:
    situação = "Recuperação!"
else: 
    situação = "Reprovado!"

match situação:
    case "Parabéns!":
        print("Aprovado!")
        print("Parabéns!")
    case "Recuperação!":
        print("Recuperação!")
    case "Reprovado!":
        print("Reprovado!")

