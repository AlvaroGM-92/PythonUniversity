class Aritmetica:
    def __init__(self,operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        print(f'Suma: {self.operando1 + self.operando2}')

    def restar(self):
        print(f'Resta: {self.operando1 - self.operando2}')

    def multiplicar(self):
        print(f'Multiplica: {self.operando1 * self.operando2}')

    def dividir(self):
        if self.operando2 != 0:
            print(f'Dividir: {self.operando1 / self.operando2}')
        else:
            print('No se puede dividir entre 0')

if __name__== '__main__':
    print('--- Primer objeto ---')
    operacion1 = Aritmetica(5, 7)
    operacion1.sumar()
    operacion1.restar()
    operacion1.multiplicar()
    operacion1.dividir()
    print()

    print('--- Segundo objeto ---')
    operacion2 = Aritmetica(12, 16)
    operacion2.sumar()
    operacion2.restar()
    operacion2.multiplicar()
    operacion2.dividir()