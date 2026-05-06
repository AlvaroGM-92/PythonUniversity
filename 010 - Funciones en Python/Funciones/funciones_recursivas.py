print('*** Imprimir del 1 al 5 de forma recursiva ***')

# Definir la funcion recursiva
def funcion_recursiva(numero):
    if numero == 1:
        print(numero, end=' ') # 1
    else: # Caso recursivo
        # print(numero, end=' ') # Si se imprime antes de restarlo, se realizará al contrario, irá de mayor a menor
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

# Programa principal
funcion_recursiva(5)