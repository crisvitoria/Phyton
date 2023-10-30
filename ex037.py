# 37: Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


def conversor (op,decimal):
    if op == 1: #binário
        print(f'O número convertido para binário é: {decimal:b}')
    elif op == 2: #octal
        print(f'O número convertido para octal é: {decimal:o}')
    elif op == 3: #hexadecimal
        print(f'O número convertido para hexadecimal é: {decimal:X}')
    else:
        print('Opção inválida! Tente novamente')

print('='*41)
print('| C O N V E R S O R  D E  D E C I M A L |')
print('='*41)
decimal = int(input('Informe um número: '))
print('='*45)
print('| 1 - Binário | 2 - Octal | 3 - Hexadecimal |')
print('='*45)
op = int(input('Informe a opção desejada: '))
conversor(op,decimal) #chamando a função
