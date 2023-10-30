dias = float(input('\033[1;35;48m=====Aluguel de carros=====\33[m'
                   '\n\033[1;0;40mQuanto dias utilizados: \33[m'))
km = float(input('\033[1;0;40mQuantos quilomentros rodados: \33[m'))
valor = (dias * 60) + (km * 0.15)
print(f'O valor a ser pago pelo aluguel é de: R${valor:.{2}f}')
