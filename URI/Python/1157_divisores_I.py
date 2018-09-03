#coding: utf-8

"""
Ler um número inteiro N e calcular todos os seus divisores.

Entrada:
O arquivo de entrada contém um valor inteiro.

Saída:
Escreva todos os divisores positivos de N, um valor por linha.
"""

# Lendo o número inteiro.
N = int(input());

# Pra cada número entre 1 e o número informado.
for i in range(1, N + 1):
    # Se ele for divisível pelo número informado, printamos ele.
    if (N % i == 0):
        print i
