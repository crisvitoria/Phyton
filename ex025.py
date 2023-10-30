#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nomeCompleto = str(input('Informe seu nome completo:\n')).strip() #retira os espaços do início e do fim
if nomeCompleto.lower().find('silva') != -1:
    print(f'O seu nome contem "Silva"')
else:
    print('O nome informado não contem "Silva"')