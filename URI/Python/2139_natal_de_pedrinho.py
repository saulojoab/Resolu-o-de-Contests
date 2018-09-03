# coding: utf-8
import datetime

"""
Pedrinho é um garoto que adora festas em família, principalmente o Natal, quando ganha presente dos pais e dos avós.
Esse ano, seu pai lhe prometeu um PS4, mas somente se Pedrinho conseguir resolver alguns desafios ao longo do ano,
sendo um deles, escrever um programa que calcule quantos dias faltam para o Natal.

Entretanto, Pedrinho tem somente 9 anos e não tem noção alguma de programação, mas sabe que você, primo dele,
mexe com "coisas de computador", e dessa forma, pediu para você escrever o programa para ele.
Não somente isso, mas prometeu que deixaria você jogar todo final de semana e por quanto tempo quiser!

Entrada:
A entrada é composta por vários casos de teste. Cada linha contém o mês e o dia do ano de 2016 (ano bissexto).
A entrada termina com fim de arquivo.

Saída:
Se for Natal, imprima "E natal!"; se faltar somente um dia, imprima "E vespera de natal!"; se já passou,
imprima "Ja passou!". Caso contrário, imprima "Faltam X dias para o natal!",
sendo X o número de dias que faltam para o Natal.
"""
while True:
    # Precisa fazer um try pra poder fazer o EOF (fim do arquivo).
    try:
        # Recebendo o mes e o dia do usuário.
        mes, dia = map(int, raw_input().strip().split());

        # Caso seja 24/12/2016.
        if (mes == 12 and dia == 24):
            print "E vespera de natal!";
        # Caso seja 25/12/2016.
        elif (mes == 12 and dia == 25):
            print "E natal!";
        # Caso já tenha passado o natal.
        elif (mes > 12 or (mes == 12 and dia > 24)):
            print "Ja passou!";
        # Caso o natal ainda não tenha passado..
        else:
            # Criando a data informada pelo usuário e a data do natal.
            data = datetime.date(2016, mes, dia);
            natal = datetime.date(2016, 12, 24)

            # Calculando quantos dias existem entre essas duas datas.
            diasQueFaltam = (natal - data).days + 1;

            # Mostrando o resultado ao usuário.
            print "Faltam {} dias para o natal!".format(diasQueFaltam);
    except EOFError:
        break;