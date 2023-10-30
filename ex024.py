#024: Crie um programa que leia o nome de uma cidade diga se ela começa
#ou não com o nome "SANTO".
cidade = input('Informe o nome da cidade: ').strip()
if cidade.lower().find('santo') == 0:
    print(f'A cidade começa com o nome "Santo".')
else:
    print('A cidade não começa com a palavra "Santo".')