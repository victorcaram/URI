import sys

nome = raw_input();
salario = input();
vendas = input();

total = salario + (vendas * 0.15)

print("TOTAL = R$ " + "{0:.2f}".format(round(total,2)))