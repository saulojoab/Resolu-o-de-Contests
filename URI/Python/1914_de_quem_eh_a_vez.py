# coding: utf-8
import math

"""
Amarelinha provavelmente é a brincadeira em que as crianças da vila mais se divertem, porém a mesma vem causando um 
bom tempo de discussão e choro nas crianças que a praticam. A causa do transtorno é para decidir quem 
será o próximo a pular, mas recentemente Quico (O gênio!) teve uma grande ideia para solucionar o problema. 
Basicamente a brincadeira só poderá ser jogada de dois em dois jogadores e para escolher o próximo jogador 
Quico indicou o uso do tradicional método par ou ímpar, onde os dois jogadores informam um número e se a soma 
desses números for par o jogador que escolheu PAR ganha ou vice verso. Entretanto a utilização desse método vem 
deixando o Quico louco, louco, louco... E por esse motivo ele pediu a sua ajuda! Solicitou a você um programa que 
dado o nome dos jogadores, suas respectivas escolhas PAR ou IMPAR e os números, informe quem foi o vencedor.

A primeira linha de entrada contém um número inteiro QT (1 ≤ QT ≤ 100),
indicando a quantidade de casos de teste que vem a seguir. Cada caso de teste contém duas linhas.
Na primeira linha será informado o nome do jogador 1 seguido de sua escolha,
“PAR” ou “IMPAR” e logo após, o nome do jogador 2 seguido de sua escolha, “PAR” ou “IMPAR”.
Na segunda linha de entrada, contém 2 números inteiros N (1 ≤ N ≤ 10⁹) e M (1 ≤ M ≤ 10⁹), representando respectivamente
os números escolhidos pelo jogador 1 e pelo jogador 2. É garantido que a escolha (PAR ou IMPAR) do jogador 1 será
diferente da escolha (PAR ou IMPAR) do jogador 2 e que o nome dos jogares são formados somente por letras e
não ultrapassarão 100 caracteres.
"""

QT = int(input());

# Se a quantidade de repetições for maior ou igual à um e menor ou igual a 100.
if ((1 <= QT) and (QT <= 100)):
    # Repetir de acordo com o número de repetições informado.
    for i in range(0, QT):
        # Recebe os nomes e escolhas do usuário.
        nome1, escolha1, nome2, escolha2 = map(str, raw_input().split());
        # Recebe os dois números do usuário.
        n1, n2 = map(int, raw_input().strip().split())

        # Caso os dois números estejam entre 1 e 10 elevado à nona.
        if ((1 <= n1 <= math.pow(10, 9)) and (1 <= n2 <= math.pow(10, 9))):
            # Se a soma dos números informados for par.
            if ((n1 + n2) % 2 == 0):
                # Verificando quem escolheu par.
                if (escolha1 == "PAR"):
                    print nome1
                elif (escolha2 == "PAR"):
                    print nome2
            # Se a soma dos números informados for ímpar.
            else:
                # Verificando quem escolheu ímpar.
                if (escolha1 == "IMPAR"):
                    print nome1
                elif (escolha2 == "IMPAR"):
                    print nome2
