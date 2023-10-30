#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = input('Informe um número de 0 a 9999: ')
tamanho = len(numero)
if tamanho <= 4:
    if tamanho == 1:
        print(f'Unidade: {numero[0]}')
    elif (tamanho > 1) and (tamanho <= 2):
        print(f'Unidade: {numero[1]}\nDezena: {numero[0]}')
    elif (tamanho > 2) and (tamanho <= 3):
        print(f'Unidade: {numero[2]}\nDezena: {numero[1]}\nCentena: {numero[0]}')
    else:
        print(f'Unidade: {numero[3]}\nDezena: {numero[2]}\nCentena: {numero[1]}\nMilhar: {numero[0]}')
else:
    print('Informe um número válido!')