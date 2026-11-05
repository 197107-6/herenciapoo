from clases.paqueteria import Envio, EnvioExpress, EnvioSobre

def main():
    envio = Envio("Juan", 10)
    sobre = EnvioSobre("Maria")
    envioExpress = EnvioExpress("Pedro", 20)

    print(envio.resumen())
    print(sobre.resumen())
    print(envioExpress.resumen())

if __name__ == "__main__":
    main()
