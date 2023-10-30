#31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 parta viagens mais longas.
distViagem = float(input('Informe a distância de uma viagem: '))
passagem = distViagem * 0.50 if distViagem < 201 else distViagem * 0.45
'''if distViagem < 201:
    passagem = float(distViagem * 0.50)
else:
    passagem = float(distViagem * 0.45)'''
print(f'Sua viagem custará: R${passagem:.{2}f}')