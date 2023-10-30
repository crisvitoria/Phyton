#34: Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Informe o salário atual: '))
if sal > 1250:
    print(f'O novo salário será R$ {(sal + (sal * 0.10)):.{2}f}\nO aumento foi de 10%')
else:
    print(f'O novo salário será R${(sal + (sal * 0.15)):.{2}f}\nO aumento foi de 15%')