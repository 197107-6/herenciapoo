from clases.empleados import Empleado,EmpleadoPorHoras,Vendedor
def main():
    empleado = Empleado("Jerome", 2500)
    vendedor = Vendedor("Juan", 2500, 1000)
    empleado_horas = EmpleadoPorHoras("Ana", 20, 100)

    print(empleado.descripcion())
    print(vendedor.descripcion())
    print(empleado_horas.descripcion())

if __name__ == "__main__":
    main()