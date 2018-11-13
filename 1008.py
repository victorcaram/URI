import sys

numero = input();
horas = input();
valorPhora = input();

salario = (horas * valorPhora)

print("NUMBER = " + str(numero))
print("SALARY = U$ " + "{0:.2f}".format(round(salario,2)))