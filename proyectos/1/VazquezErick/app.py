from modelo import Modelo
from vista import Vista
from controlador import Controlador


def main():
    controlador = Controlador()
    modelo = Modelo(controlador)
    vista = Vista(controlador)
    
    modelo.start()
    vista.inicia_interfaz()
    
if __name__ == "__main__":
    main()