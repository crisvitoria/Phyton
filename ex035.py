#35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
#importando bibliotecas
import colorama
#declaração de funçoes
def formaTriangulo (seg1,seg2,seg3):
    #função que verifica se os valores informados formam um triângulo
    if (seg1 + seg2 > seg3) and (seg1 + seg3 > seg2) and (seg2 + seg3 > seg1):
        return print(colorama.Fore.YELLOW+f'Os seguimentos informados formam um triâgulo!')
    else:
        return print(colorama.Fore.RED+f'Os segmentos informados não são capazes de formar um triângulo!')
#inicio do programa
print(colorama.Fore.BLUE + '-*-' * 15)
print('*        Analisando       Triângulos        *')
print('-*-' * 15)
print(colorama.Fore.GREEN)
seg1 = float(input('Informe o 1º seguimento: '))
seg2 = float(input('Informe o 2º seguimento: '))
seg3 = float(input('Informe o 3º seguimento: '))
formaTriangulo(seg1,seg2,seg3)