# 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

import colorama
print(colorama.Fore.RED + '*'*31)
print('*            RADAR            *')
print('*'*31)
print(colorama.Style.RESET_ALL)
velocidade = int(input('Informe a velocidade do carro: '))
if velocidade > 80:
    multa = float((velocidade - 80)*7)
    print(colorama.Fore.RED + f'Você ultrapassou o limite de velocidade de 80km/h!\nO valor da sua milta é de R${multa:.{2}f}')
else:
    print(colorama.Fore.GREEN + f'Tenha um bom dia! Dirija com segurança')