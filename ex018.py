from math import radians,sin,cos,tan
angulo = float(input('Informe o ângulo: '))
print(f'Com base no ângulo de {angulo}º graus, os dados equivalentews são:\n'
      f'Seno = {sin(radians(angulo)):.{2}f}\nCosseno = {cos(radians(angulo)):.{2}f}\n'
      f'Tangente = {tan(radians(angulo)):.{2}f}')