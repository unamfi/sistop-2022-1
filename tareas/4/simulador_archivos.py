

"""Estructura de un archivo
Nombre
Contenido 
Tamano
Modo
"""
class File: 

    def __init__(self) -> None:
        self.name
        self.data
        self.size






FILE_NAME = "informacion_uso.txt"

try: 
    f = open(FILE_NAME, "r")
except:
    print(f"ERROR: no se ha encontrado el archivo {FILE_NAME}")
    exit(1)

print("Simulador: \n")

info = f.read()
print(info)

print("\n")

while True: 
    print("-> ", end="")

    in = input()

    command = in.split(" ")

    print("\n")
    #print(comando)

    action = command[0]

    if action == "dir":
        pass
    elif action == "open":
        pass
    elif action == "close":
        pass
    elif action == "read":
        pass
    elif action == "write":
        pass
    elif action == "seek":
        pass
    elif action == "quit": 
        break
    else: 
        print("Comando incorrecto.\n")
        print(contenido)

