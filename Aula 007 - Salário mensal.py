'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas.
Calcule e mostre o total do seu salário no referido mês.
'''

salario_hora = float(input("Informe o seu salário por hora: "))
horas_trabalhadas = int(input("Informe o número de horas trabalhadas por mês: "))

salario_mensal = salario_hora * horas_trabalhadas
print("")

print(f"O seu salário mensal é: R$ {salario_mensal:.2f}")