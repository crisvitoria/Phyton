#30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Informe um número: '))
if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')