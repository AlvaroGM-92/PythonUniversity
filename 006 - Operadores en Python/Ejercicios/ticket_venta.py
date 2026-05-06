print('*** Generacion Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio platanos: '))

descuento = float(input('Descuento: ')) / 100

# Calculo del subtotal (sin impuestos)
subtotal_sin_descuento = precio_leche + precio_pan + precio_lechuga + precio_platanos

descontado = subtotal_sin_descuento * descuento

subtotal_con_descuento = subtotal_sin_descuento - descontado

# Calculo con impuestos (16%)
impuesto_sin_descuento = subtotal_sin_descuento * 0.16
impuesto_con_descuento = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuestos)
costo_total_compra_sin_descuento = subtotal_sin_descuento + impuesto_sin_descuento
costo_total_compra_con_descuento = subtotal_con_descuento + impuesto_con_descuento
print(f'''
Subtotal: ${subtotal_sin_descuento:.2f}
Descuento: {descuento}
Descontado: {descontado}
Subtotal con descuento: {subtotal_con_descuento}
Impuesto sin descuento (16%): {impuesto_sin_descuento:.2f}
Impuesto con descuento (16%): {impuesto_con_descuento}
Costo total de la compra sin descuento: ${costo_total_compra_sin_descuento:.2f}
Costo total de la compra con descuento: ${costo_total_compra_con_descuento}''')