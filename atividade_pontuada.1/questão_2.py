# Questão 2:
# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).
# Por fim, mostre os dados do usuário.

import os
os.system("clear")

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estado_civil = input("Digite seu estado civil: ")

sexo = "F"
match estado_civil:
    case "Casada" | "casada":
        anos_de_casada = int(input("Digite quantos anos de casada: "))
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado civil: {estado_civil}")
        print(f"anos de casada: {anos_de_casada}")

sexo = "F"
match estado_civil:        
    case "Solteira" | "solteira":
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado civil: {estado_civil}")
              
sexo = "M"
match estado_civil:
    case "Solteiro" | "solteiro" | "Casado" | "casado":
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado civil: {estado_civil}")
    
    

    