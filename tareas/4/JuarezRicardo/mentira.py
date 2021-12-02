class Archivo:
    def __init__(self, nombre, datos) -> None:
        self.nombre = nombre
        self.datos = datos


def main():
    mentira1 = Archivo("m1.lie","1111111111111")
    mentira2 = Archivo("m2.lie","2222222222222")
    mentira3 = Archivo("m3.lie","3333333333333")
    mentira4 = Archivo("m4.lie","4444444444444")

    archivos = [mentira1, mentira2, mentira3, mentira4]
    help = '\n\n\ndir -> Muestra el directorio\n\nopen <arch> <modo> -> Especifica que operaremos con el archivo denombre "arch", empleando el modo especificado. Entrega un descriptor de archivo numérico.\n\nclose <descr> -> Termina una sesión de trabajo con el archivo referido por el descriptor indicado. Después de un close, cualquier intento por usar ese archivo entregará error.\n\nread <descr> <longitud> -> Lee la cantidad de bytes especificada\n\nwrite <descr> <longitud> <datos> -> Escribe la cantidad de bytes especificada, guardando los datos indicados como parámetro.\n\nseek <descr> <ubicacion> -> Salta a la ubicación especificada del archivo.\n\nquit -> Detiene la ejecución de la simulación\n\n\n\n' 
    print("Simulacion de sistema de archivos.")
    print("Escribe 'ayuda' y enter para ver los comandos disponibles.")

    while 1:
        print(">", end="")
        commando = input()
        c = commando.split()

        if c[0] == 'read':
            print("lee archivo")


        elif c[0] == 'dir':
            print(" ")
            for a in archivos:
                print(a.nombre + "  ", end="")
            print("\n")

        elif c[0] == 'open':
            noarch = len(archivos)
            i = 0
            for a in archivos:
                if c[1] == a.nombre:
                    if c[2] == "r":
                        print(a.datos)
                        break
                    else:
                        print("error: no está en modo lectura")
                        break
                else:
                    i = i+1
                    if i >= noarch:
                        print("Error: archivo no encontrado")
                        break
                
        elif c[0] == 'ayuda':
            print(help)
            
        elif c[0] == 'quit':
            break

if __name__ == "__main__":
    main()