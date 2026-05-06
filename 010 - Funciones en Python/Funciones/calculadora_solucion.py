print('*** Calculadora con Funciones ***')

def mostrar_menu():
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicar
    4. Dividir
    5. Salir''')
    return int(input('Escoge una opcion: '))

def pedir_valores():
    operando1 = float(input('Dame el valor 1: '))
    operando2 = float(input('Dame el valor 2: '))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    # Solicitar los valores de los operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1: # Sumar
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}')
    elif opcion == 2: # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}')
    elif opcion == 3: # Multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado}')
    elif opcion == 4: # Division
        if operando2 != 0:
            resultado = operando1 / operando2
            print(f'El resultado de la division es: {resultado}')
        else:
            print('No se puede diviidir entre 0')
    elif opcion == 5: # Salir
        print('Saliendo del programa de calculadora, hasta pronto!')
        salir = True
    else:
        print('Opcion invalida, selecciona optra opcion...\n')
    return salir

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)