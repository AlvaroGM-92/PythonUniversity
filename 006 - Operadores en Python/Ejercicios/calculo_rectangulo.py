print('*** Area y Perimetro de un Rectangulo ***')

base = float(input('Introduce el valor de la BASE: '))
altura = float(input('Introduce el valor de la ALTURA: '))

area = base * altura
perimetro = 2 * (base + altura)

print(f'''\nArea y perimetro
Area: {area}
Perimetro: {perimetro}''')