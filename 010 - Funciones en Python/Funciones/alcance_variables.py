print('*** Alcance de Variables ***')

contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0

    # usar la variable goblal
    global contador_global
    contador_global += 1

    # incremetar la variable local
    contador_local += 1

    # Imprimir ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# llamamos varias veces la funcion
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'Valor variable global: {contador_global}')
