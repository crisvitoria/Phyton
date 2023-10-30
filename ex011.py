altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura*largura
print(f'Área total da parede: {area:.{2}f}')
if area / 2 <= 1:
    print(f'Será necessária {area/2:.{0}f} lata de tinta para pintar a parede')
else:
    print(f'Serão necessárias {area / 2:.{0}f} latas de tinta para pintar a parede')