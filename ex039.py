#39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo.

from datetime import datetime, date
from time import sleep

def verifica_alistamento(dias,dataDez):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_finais = dias_restantes % 30
    if anos >= 18:
        print('Você já fez 18 anos e ultrapassou o prazo para se alistar!')
        print(f'Você tem {anos} anos, {meses} meses e {dias_finais} dias')
        if anos == 18:
            if meses > 0:
                print(f'Você excedeu seu prazo em: {meses} meses, e {dias_finais} dias')
            else:
                print(f'Você excedeu seu prazo em: {dias_finais} dias')
        else:
            if meses > 0:
                print(f'Você excedeu seu prazo em: {anos-18} anos, {meses} meses, e {dias_finais} dias')
            else:
                print(f'Você excedeu seu prazo em: {anos-18} anos, {dias_finais} dias')
    else:
        print('Você ainda não completou 18 anos!')
        print(f'Você tem {anos} anos, {meses} meses e {dias_finais} dias')
        tempos = dataDez - dataHoje
        dias = tempos.days
        anos = dias // 365
        dias_restantes = dias % 365
        meses = dias_restantes // 30
        dias_finais = dias_restantes % 30
        if anos > 0:
            print(f'Você tem o prazo de {anos} anos, {meses} meses e {dias_finais} dias')
        elif meses > 0:
            print(f'Você tem o prazo de {meses} meses e {dias_finais} dias')
        else:
            print(f'Você tem o prazo de {dias_finais} dias')


#ano = int(input('Informe seu ano de dascimento: '))
#mes = int(input('Informe seu mes de dascimento: '))
#dia = int(input('Informe seu dia de dascimento: '))
nasc = input('Informe sua data de nascimento (xx/xx/xxxx): ')
dia, mes, ano = map(int, nasc.split('/'))
dataNasc = datetime(ano,mes,dia) #transformando em data
dataHoje = datetime.now() #buscando a data de hoje
dataDezoito = datetime(ano+18,mes,dia) #descobre a data que fará 18 anos
tempo = dataHoje - dataNasc #calculando a diferenca entre as datas
tempo = tempo.days
verifica_alistamento(tempo,dataDezoito)


