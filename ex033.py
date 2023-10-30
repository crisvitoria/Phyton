
lim = int(input('Quantos números deseja informar: '))
numeros = []
while lim != 0:
    numero = float(input('Informe o número: '))
    numeros.append(numero)
    lim -= 1
print(f'O maior número informado foi o {max(numeros):.{2}f}')
print(f'O menor número informado foi o {min(numeros):.{2}f}')