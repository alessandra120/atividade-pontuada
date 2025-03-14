import os
os.system("clear")

renda_mensal = float(input("Informe a sua renda mensal: R$ "))
valor_emprestimo = float(input("Informe o valor total do empréstimo solicitado: R$ "))
prestacoes = int(input("Informe o número de prestações: "))

    
limite_emprestimo = 10 * renda_mensal
prestacao_mensal = valor_emprestimo / prestacoes
limite_prestacao = 0.30 * renda_mensal

    
if valor_emprestimo <= limite_emprestimo and prestacoes <= limite_prestacao:
    print("Empréstimo pode ser concedido!")
else:
    print("Empréstimo não pode ser concedido!")