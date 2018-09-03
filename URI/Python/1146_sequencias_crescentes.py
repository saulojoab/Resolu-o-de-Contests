# coding: utf-8

"""
Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de
entrada for igual a zero). Para cada valor lido imprima a sequência de 1 até X,
com um espaço entre cada número e seu sucessor.

Obs: cuide para não deixar espaço em branco após o último valor apresentado na linha ou você receberá Presentation Error.

Entrada
O arquivo de entrada contém vários números inteiros. O último número no arquivo de entrada é 0.

Saída
Para cada número N do arquivo de entrada deve ser impressa uma linha de 1 até N, conforme o exemplo abaixo.
Não deve haver espaço em branco após o último valor da linha.
"""

# Inicializando a variável X. Esse valor não importa contanto que não seja 0.
X = 3;

while (X != 0):
    # Recebendo o valor do usuário.
    X = int(input());

    # Pra cada número entre 1 e o número do usuário.
    for i in range(1, X + 1):
        # Enquanto não chegar no último número, printamos sem quebrar a linha.
        if (i != X):
            print i,
        # Quando chegar no último número, printamos e quebramos a linha.
        else:
            print i