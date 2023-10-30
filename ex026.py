#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
print(f'A frase "{frase}" tem {frase.replace('á','a').replace('à','a').lower().count('a')} letras "A".')
print(f'A primeira ocorrencia da letra "A" é na {frase.replace('á','a').replace('à','a').lower().find('a')+1}ª posição')
print(f'A ultima ocorrencia da letra "A" é na {frase.replace('á','a').replace('à','a').lower().rfind('a')+1}ª posição')