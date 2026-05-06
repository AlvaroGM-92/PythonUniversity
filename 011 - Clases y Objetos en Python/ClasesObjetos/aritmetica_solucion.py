class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado de la suma: {resultado}')

    def resta(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado de la resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado de la multiplicacion: {resultado}')

    def dividir(self):
        if self.operando2 != 0:
            resultado = self.operando1 / self.operando2
            print(f'Resultado de la division: {resultado}')
        else:
            print('No es posible dividir entre 0')

# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Aritmetica ***')
    print('Primer Objeto')
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.resta()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    print()

    # Segundo objeto
    print('Segundo Objeto')
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.resta()
    aritmetica2.multiplicar()
    aritmetica2.dividir()