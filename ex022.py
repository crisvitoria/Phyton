#/*022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nomeC = str(input('Informe seu nome completo: ')).strip()
print(f'Maiúculas: {nomeC.upper()}')
print(f'Minúsculas: {nomeC.lower()}')
print(f'O nome completo tem {len(nomeC.replace(" ",""))} letras')
nomes = nomeC.split()
print(f'O seu primeiro nome é {nomes[0].upper()} e tem {len(nomes[0])} letras')