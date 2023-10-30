#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
#o primeiro e o último nome separadamente.

nomeCompleto = str(input('Informe seu nome completo: ')).strip()
nomes = nomeCompleto.split() #função para separar a frase em palavras
print(f'O seu primeiro nome é {nomes[0].capitalize()}')
print(f'O seu último nome é {nomes[-1].capitalize()}')