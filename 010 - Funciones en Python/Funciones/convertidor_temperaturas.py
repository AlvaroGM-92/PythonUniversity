print('*** Conversor de Temperaturas ***')

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) *5 / 9

# Realizamos algunas pruebas de converion
celsius = float(input('Proporcione su valor en Celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'- {celsius} C a F: {resultado:.2f}')

# Realizamos la prueba de grados fahrenhei a celsius
fahrenheit = float(input('Proporcione su valor en Fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'- {fahrenheit} C a F: {resultado:.2f}')