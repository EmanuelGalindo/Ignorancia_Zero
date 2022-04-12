'''
Faça um programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
    notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
    três notas de 100, uma nota de 50, quatro notas de 10,
    uma nota de 5 e quatro notas de 1.
'''

import sys

valor = float(input("Informe o valor do saque (mínimo: R$ 10.00 / máximo: R$ 600.00): "))
valor_fixo = valor

if (valor < 10) or (valor > 600):
    print("Um valor menor que R$ 10.00 ou maior que R$ 600.00 foi informado. Por favor, reinicie o programa e tente novamente.")
    sys.exit()
print("")

lista100 = []
lista50 = []
lista10 = []
lista5 = []
lista1 = []

if valor - 100 >= 0:
    while valor - 100 >= 0:
        lista100.append(valor)
        valor = valor - 100
contagem100 = len(lista100)

if valor - 50 >= 0:
    while valor - 50 >= 0:
        lista50.append(valor)
        valor = valor - 50
contagem50 = len(lista50)

if valor - 10 >= 0:
    while valor - 10 >= 0:
        lista10.append(valor)
        valor = valor - 10
contagem10 = len(lista10)

if valor - 5 >= 0:
    while valor - 5 >= 0:
        lista5.append(valor)
        valor = valor - 5
contagem5 = len(lista5)

if valor - 1 >= 0:
    while valor - 1 >= 0:
        lista1.append(valor)
        valor = valor - 1
contagem1 = len(lista1)

print(f'''Para sacar a quantia de R$ {valor_fixo:.2f} serão necessárias:
- {contagem100} cédula(s) de R$ 100.00;
- {contagem50} cédula(s) de R$ 50.00;
- {contagem10} cédula(s) de R$ 10.00;
- {contagem5} cédula(s) de R$ 5.00;
- {contagem1} moeda(s) de R$ 1.00.
''')