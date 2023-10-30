from random import choice
i = 0
nomes = []
while i < 4:
    nome = input(f'Informe o {i+1}º nome: ')
    nomes.append(nome)
    i += 1

#print('Os nomes informados foram:')
#for nome in nomes:
#    print(f'{nome}')
print(f'O nome sorteado foi: {choice(nomes)}')