# coding: utf-8

"""
Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10].
Em cada posição subsequente, coloque o dobro do valor da posição anterior.
Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente.
Mostre o vetor em seguida.

Entrada:
A entrada contém um valor inteiro (V<=50).

Saída:
Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i.
O primeiro número do vetor N (N[0]) irá receber o valor de V.
"""

# Recebendo o valor do usuário.
V = int(input());
# Inicializando o vetor (na verdade é uma lista) com 10 posições vazias.
N = [None] * 10;

# Caso o valor que o usuário informou for menor ou igual que 50.
if (V <= 50):
    # Pra cada número entre 0 e a quantidade de posições no vetor.
    for i in range(0, N.__len__()):
        # Adiciona V no vetor.
        N.append(V);
        # Printa (com formatação) o que foi requisitado.
        print "N[{}] = {}".format(i, V);
        # Multiplica o valor de V por dois.
        V *= 2;