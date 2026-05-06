class Aritmetica:
    def __init__(self,operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        print(f'Suma: {self._operando1 + self._operando2}')

    def restar(self):
        print(f'Resta: {self._operando1 - self._operando2}')

    def multiplicar(self):
        print(f'Multiplica: {self._operando1 * self._operando2}')

    def dividir(self):
        if self._operando2 != 0:
            print(f'Dividir: {self._operando1 / self._operando2}')
        else:
            print('No se puede dividir entre 0')

    @property
    def operando1(self):
        return self._operando1

    @property
    def operando2(self):
        return self._operando2

    @operando1.setter
    def operando1(self,operando1):
        self._operando1 = operando1

    @operando2.setter
    def operando2(self,operando2):
        self._operando2 = operando2

if __name__== '__main__':
    print('--- Primer objeto ---')
    operacion1 = Aritmetica(5, 7)
    print(f'Valor operando1 del objeto operacion1: {operacion1.operando1}')
    print(f'Valor operando2 del objeto operacion2: {operacion1.operando2}')
    operacion1.sumar()
    operacion1.restar()
    operacion1.multiplicar()
    operacion1.dividir()
    operacion1.operando1 = 9
    operacion1.operando2 = 15
    print(f'Valor operando1 del objeto operacion1: {operacion1.operando1}')
    print(f'Valor operando2 del objeto operacion2: {operacion1.operando2}')
    operacion1.sumar()
    operacion1.restar()
    operacion1.multiplicar()
    operacion1.dividir()

    print()

    print('--- Segundo objeto ---')
    operacion2 = Aritmetica(12, 16)
    print(f'Valor operando1 del objeto operacion2: {operacion2.operando1}')
    print(f'Valor operando2 del objeto operacion2: {operacion2.operando2}')
    operacion2.sumar()
    operacion2.restar()
    operacion2.multiplicar()
    operacion2.dividir()