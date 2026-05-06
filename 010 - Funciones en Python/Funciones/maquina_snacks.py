print('*** Maquina de Snacks ***')

# Definimos la lista de snacks inicial
snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos comprados
productos = []

def mostrar_snacks():
    print('\n--- Snacks Disponibles---')
    for snack in snacks:
        print(f'\tId: {snack.get('id')} -> {snack.get("nombre")} - ${snack.get("precio")}')

def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('id') == id_buscar:
            return snack
        else: # Si llegamos al final y no se econtro el snack regresa None
            return None


def comprar_snack():
    id_snack = int(input('Que snack quieres comprar(id): '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack no encontrado con el id: {id_snack}')

def mostrar_ticket():
    ticket = f'\t--- Ticket de Venta ---'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto.get('nombre')} - ${producto.get("precio")}'
        total += producto.get('precio')
    ticket += f'\n\tTotal: {total}'
    print(ticket)

# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        print(f'''\nMenu:
    1. Mostrar Snacks
    2. Comprar Snacks
    3. Mostrar Ticket
    4. Salir''')
        opcion = int(input('Escoge una opcion: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Regresa pronto!')
            break
        else:
            print('Opcion invalida, proporciona otra opcion')