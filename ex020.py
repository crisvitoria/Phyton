#informe 4 alunos e sorteie a ordem de apresentaçao
from random import shuffle
i = 0
nomes = []
while i < 4:
    nome = input(f'Informe o {i+1}º nome: ')
    nomes.append(nome)
    i += 1

shuffle(nomes) #função para embaralhar os nomes
i = 1
print('A ordem da apresentação será:')
for nome in nomes:
    print(f'{i}º {nome}')
    i +=1