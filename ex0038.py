#038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 == num2:
    print('Os números informados são iguais')
elif num1 > num2:
    print(f'O primeiro número informado ({num1}) é maior que o segundo número informado ({num2}) ')
else:
    print(f'O segundo número informado ({num2}) é maior que o primeiro número ({num1})')

