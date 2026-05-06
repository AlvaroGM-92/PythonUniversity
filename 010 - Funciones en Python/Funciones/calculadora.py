print('*** Calculadora con Funciones ***')

def mostrar_menu():
    print('''\nOperaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    return int(input('Escoge una opcion: '))

def suma():
    valor1 = float(input('Ingresa el valor 1: '))
    valor2 = float(input('Ingresa el valor 2: '))
    resultado = valor1 + valor2
    print(f'El resultado de la suma es: {resultado:.2f}')

def resta():
    valor1 = float(input('Ingresa el valor 1: '))
    valor2 = float(input('Ingresa el valor 2: '))
    resultado = valor1 - valor2
    print(f'El resultado de la resta es: {resultado:.2f}')

def multiplicacion():
    valor1 = float(input('Ingresa el valor 1: '))
    valor2 = float(input('Ingresa el valor 2: '))
    resultado = valor1 * valor2
    print(f'El resultado de la multiplicacion es: {resultado:.2f}')

def division():
    valor1 = float(input('Ingresa el valor 1: '))
    valor2 = float(input('Ingresa el valor 2: '))
    if valor2 != 0:
        resultado = valor1 / valor2
        print(f'El resultado de la division es: {resultado:.2f}')
    else:
        print('No se puede dividir por 0')

if __name__ == '__main__':
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            print('Saliendo del programa Calculadora. Hasta Pronto!')
            break
        else:
            print('Opcion no valida')
