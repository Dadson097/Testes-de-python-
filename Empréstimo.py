# Empréstimo
casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
tempo = int(input("Digite o tempo de pagamento em anos: "))
prestacao = casa / (tempo * 12)
limite = salario * 0.30
parcela = tempo * 12
print("Prestação mensal: R${:.2f}".format(prestacao))
print("Limite permitido: R${:.2f}".format(limite))
if prestacao > limite:
    print("O emprestimo foi negado!")
else:
    print("O emprestimo foi aprovado!,\nO pagamento será feito em: {} parcelas de: {:.2f}".format(parcela, prestacao))