class Empleado(object):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self):
        return self.salario_base

    def descripcion(self):
        return f"{self.nombre}: ${self.calcular_pago():.2f}"

#Hereda a la clase empleado ()

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas, comision=0.05):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
        self.comision = comision

        #polimorfismo: es la capacidad de declarar un metodo con el mismo nombre de la clase base


    def calcular_pago(self):
        return super().calcular_pago() + (self.ventas * self.comision)

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, salario_base=0)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self):
        return self.horas_trabajadas * self.tarifa_por_hora