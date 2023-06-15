print("\n\n========================================================")
print("   Cálculo de financiamento com reajuste anual de 10%   ")
print("========================================================\n\n")

valor_parcela = float(input("Digite o valor da primeira parcela: "))
quantidade_meses = int(input("Digite o total de meses: "))
taxa_juros = float(input("Digite a taxa de juros (em % porém sem o sinal): ")) / 100

valor_total = 0
parcela_atual = valor_parcela

for i in range(1, quantidade_meses + 1):
    valor_total += parcela_atual
    if i % 12 == 0:
        parcela_atual *= (1 + taxa_juros)

valor_ultima_parcela = parcela_atual
valor_total_formatado = "{:.2f}".format(valor_total)
valor_ultima_parcela_formatado = "{:.2f}".format(valor_ultima_parcela)

print("\n\n==============================")
print("          Resultado             ")
print("==============================\n")
print("O valor total pago em", quantidade_meses, "meses é de: R$", valor_total_formatado)
print("O valor da última parcela é de: R$", valor_ultima_parcela_formatado)
