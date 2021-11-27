import sys
import copy

"""
Estructura de un archivo
- Nombre
- Contenido 
- Tamano
- Modo
"""

class ExceptionNumArgs(Exception):
    def __init__(self, action) -> None: 
        super(ExceptionNumArgs, self).__init__(f"ERROR: el numero de argumentos para la operacion '{action}' no es la indicada.")

class ExceptionModeType(Exception):
    def __init__(self, msj) -> None:
        super(ExceptionModeType, self).__init__(msj)

class ExceptionStringSize(Exception):
    def __init__(self, msj) -> None:
        super(ExceptionStringSize, self).__init__(msj)

class File: 

    """Estructura de simular archivos en el programa"""

    def __init__(self, name) -> None:
        self.name = name
        self._data = ""
        self.mode = None
        self.id = None
        self.status = "close"
        self.pos = 0

    #getters and setters

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    # methods

    def open(self, mode, id) -> str: 
        if self.status == "open":
            return f"El archivo {self.name}, ya esta abierto."

        self.mode = mode
        self.id = id
        self.status = "open"
        return f"Archivo abierto ({self.mode}). -> {self.id}"
         
    def close(self) -> None: 
        self.status = "close"
        self.id = None
        self.mode = None

    def read(self, lenght) -> str:
        if self.mode == "R":
            res = "" 
            count = 0
            for chr in self.data: 
                if count == lenght or count == len(self.data):
                    break
                res += chr
                count += 1

            return res
        else: 
            raise ExceptionModeType(f"ERROR: el archivo '{self.name}' está abierto en modo ({self.mode})")

    def write(self, lenght, string):
        if self.pos == 0:
            self.data += string
        else:
            aux_data = list(self.data)
            aux_string = list(string)
            #print(aux_data, aux_string)
            #print(len(aux_data), lenght)

            try:   
                for i in range(lenght): 
                    aux_data[self.pos + i] = copy.copy(aux_string[i])
                    aux_string[i] = None
                self.data = "".join(aux_data)

            except IndexError:
                self.data = "".join(aux_data)
                string = "".join(list(filter(lambda x: x != None, aux_string)))
                #print(string)
                self.data += string 

    def seek(self, pos):
        #Si te manda una posicion mayor al # de caracteres del archivo, lo coloca al final. 
        if pos >= len(self.data) - 1: 
            self.pos = len(self.data) - 1
        else: 
            self.pos = pos

    def size( self ) -> int:
        return sys.getsizeof( self.data )

    def __str__(self) -> str:
        return f"{self.name}  [{self.size()} bytes]"


# functions

def dir(file_list) -> None:
    for i in range(len( file_list )):
        print(file_list[ i ], end="    ")

def busqueda_archivo(file_list, name) -> File:
    for i in range(len(file_list)):
        if file_list[ i ].name == name:
            return file_list[i]
    
    return None

def busqueda_archivo_por_id(file_list, id) -> File:
    for i in range(len(file_list)):
        if file_list[ i ].id == id:
            return file_list[i]
    
    return None

def inicialize() -> list: 

    list = []
    #arch1 [15441 bytes]    arch2 [200 bytes]      otro_mas [2048 bytes]

    a1 = File( "arch1" )
    a1.data = "Hola!"

    a2 = File( "arch2" )
    a2.data = "Hola mundo"

    a3 = File( "arch3" )
    a3.data = "Saquenos 10 porfa"

    list.append( a1 )
    list.append( a2 )
    list.append( a3 )

    return list

# Const
FILE_NAME = "informacion_uso.txt"

def main():
    # main function 
    try: 
        f = open( FILE_NAME, "r" )
    except:
        print( f"ERROR: no se ha encontrado el archivo { FILE_NAME }" )
        exit(1)

    file_list = inicialize()

    print("Simulador: \n")

    info = f.read()
    print(info)

    counter = 1

    while True:
        print("\n-> ", end="")

        command = input()
        command = command.split(" ")

        #print(command)

        action = command[0]

        if action == "dir":
            dir(file_list)

        elif action == "open":
            try: 
                if len(command) == 3: 
                    f = busqueda_archivo(file_list, command[1])
                    mode = command[2]
                    if mode != "R" and mode != "W" and mode != "M":
                        raise ExceptionModeType("ERROR: el tipo de apertura es invalido.\nR <- read   W <- write   M <- modified")

                    if f != None: 
                        #print(f, f.data)
                        res = f.open(mode, counter)
                        print(res)
                        counter += 1
                    else: 
                        #Creamos un archivo nuevo 
                        f = File(command[1])
                        file_list.append(f)
                        print(f"Se ha creado un nuevo archivo vacio con nombre '{f.name}'")
                        res = f.open(mode, counter)
                        print(res)
                        counter += 1
                else: 
                    raise ExceptionNumArgs("open")
            except ExceptionNumArgs as e: 
                print(e)
            except ExceptionModeType as e: 
                print(e)

        elif action == "close":
            try: 
                if len(command) == 2:
                    f = busqueda_archivo_por_id(file_list, int(command[1]))
                    if f != None: 
                        f.close() 
                else: 
                    raise ExceptionNumArgs("close")
            except ExceptionNumArgs as e: 
                print(e)
            except ValueError:
                print("ERROR: El descriptor del archivo debe de ser un numero.")
            
        elif action == "read":
            try: 
                if len(command) == 3:
                    f = busqueda_archivo_por_id(file_list, int(command[1]))
                    if f != None: 
                        #print(f, f.data)
                        res = f.read(int(command[2]))
                        print(res)
                    else: 
                        print("ERROR: el archivo no esta abierto")
                else: 
                    raise ExceptionNumArgs("close")
            except ExceptionNumArgs as e: 
                print(e)
            except ValueError as e:
                print(f"ERROR: La longitud y el identificador deben de ser un numero, por favor revise la entrada.\n{e}")
            except ExceptionModeType as e: 
                print(e)

        # write <descr> <longitud> <texto> 
        # si la longitud no es igual al tamanio texto, regresa un error
        # comienza a escribir desde la ultima posicion o en la que se le mueva con seek
        elif action == "write":
            try: 
                if len(command) == 4:
                    f = busqueda_archivo_por_id(file_list, int(command[1]))
                    if f != None: 
                        #Comprueba si la longitud es la misma que el tamanio de la cadena
                        lenght = int(command[2])
                        string = command[3]
                        if len(string) != lenght: 
                            raise ExceptionStringSize("ERROR: el tamanio de la cadena es distinto a la longitud especificada")
                        #print(f, f.data)
                        f.write(lenght, string)
                    else: 
                        print("ERROR: el archivo no esta abierto")
                else: 
                    raise ExceptionNumArgs("close")
            except ExceptionNumArgs as e: 
                print(e)
            except ValueError as e:
                print(f"ERROR: la longitud debe de ser un numero, por favor revise la entrada.\n{e}")
            except ExceptionStringSize as e: 
                print(e)
            
        elif action == "seek":
            try: 
                if len(command) == 3:
                    f = busqueda_archivo_por_id(file_list, int(command[1]))
                    if f != None: 
                        f.seek(int(command[2]))
                    else: 
                        print("ERROR: el archivo no esta abierto")
                else: 
                    raise ExceptionNumArgs("close")
            except ExceptionNumArgs as e: 
                print(e)
            except ValueError as e:
                print(f"ERROR: la ubicacion debe de ser un numero, por favor revise la entrada.\n{e}")        

        elif action == "info": 
            print(info)

        elif action == "quit": 
            break

        else: 
            print("Comando incorrecto.")

if __name__ == "__main__":
    main()