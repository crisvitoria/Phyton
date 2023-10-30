#36: Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. Pergunte o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar. A prestação mensal não
# pode exceder 30% do salário ou então o empréstimo será negado.

#Declaração de variáveis
print('\033[1;33;40m-*-'*15)
print('* S I M U L Ç Ã O - F I N A C I A M E N T O *')
print('-*-'*15)

#Coleta de dados
valorCasa = float(input('\033[1;37;40m Valor da casa: '))
salario = float(input(' Salário bruto do comprador: '))
anosPag = int(input(' Quantos anos o comprador irá pagar: '))

#Análise do emprestimo
prestacao = valorCasa/(anosPag*12)
if prestacao > 0.30 * salario:
    print('\033[1;31;40m-*-' * 15)
    print('*    E M P R É S T I M O    N E G A D O     *')
    print('-*-' * 15)
    print('O valor da prestação excede 30% do salário!')
    print(f'Valor da casa: RS {valorCasa:.{2}f}\n'
          f'Salário Bruto: R$ {salario:.{2}f}\n'
          f'{anosPag*12} parcelas de: R$ {prestacao:.{2}f}')
else:
    print('\033[1;32;40m-*-' * 15)
    print('*  E M P R É S T I M O    A P R O V A D O   *')
    print('-*-' * 15)
    print(f'Valor da casa: RS {valorCasa:.{2}f}\n'
          f'Salário Bruto: R$ {salario:.{2}f}\n'
          f'{anosPag*12} parcelas de: R$ {prestacao:.{2}f}')