salario = float (input('Informe seu salário atual: '))
#while (not salario.isnumeric()):
#   print('Informe um salário valido!')
#    salario = input('Informe seu salário atual: ')
#salario = float(salario)
print(f'O salário atual é: R${salario:.{2}f}\nO salário após o aumento é: R$ {salario + (salario * 0.15):.{2}f}')