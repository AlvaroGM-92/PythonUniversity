# import modulo_funcion_sumar
from modulo_funcion_sumar import sumar

print('*** Funcion sumar ***')

if __name__ == '__main__':
    # Llamar a la funcion
    resultado_funcion = sumar(8, 5)
    print(f'Resultado funcion sumar: {resultado_funcion}')

    resultado_funcion = sumar(9, 15)
    print(f'Resultado funcion sumar: {resultado_funcion}')