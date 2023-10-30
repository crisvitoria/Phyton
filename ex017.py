from math import hypot
catOp = float(input('Informe os seguintes comprimento de um triângulo retângulo:\nCateto oposto: '))
catAd = float(input('Cateto adjacente: '))
print(f'O valor da hipotenuza deste triângulo retângulo é {hypot(catOp,catAd):.{2}f}')

'''catOp = float(input('Informe os seguintes comprimento de um triângulo retângulo:\nCateto oposto: '))
catAd = float(input('Cateto adjacente: '))
hip = (catOp**2 + catAd**2) ** 0.5
print(f'O valor da hipotenuza deste triângulo retângulo é de {hip:.{2}f}')'''