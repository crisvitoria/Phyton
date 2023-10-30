#28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep
from colorama import Fore, Back, Style, init
print(Fore.RED + '-=-'*20)
print(Fore.BLUE + '    Vou pensar em um número de 0 a 5. Tente adivinhar')
print(Fore.RED + '-=-'*20)
print(Style.RESET_ALL) #apaga todos os estilos
num = int(input('Informe o número que pensei: ')) #jogador informa o número
numSort = randint(0,5) #sorteia um número de 0 a 5
print(Fore.CYAN + 'Processando...')
sleep(2)
if num == numSort:
    print(Fore.GREEN + f'Parabéns! Você venceu! Eu pensei no número {numSort} e você informou o número {num}')
else:
    print(Fore.RED + f'Você perdeu! Eu pensei no número {numSort} e você informou o número {num}')

