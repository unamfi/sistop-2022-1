
#Clase de directorios
class Directorio:
    def __init__(self, nombreD, Archivos):
        self.elementos = []
        self.nombreD = nombreD
        self.Archivos = Archivos

#Clase de archivos
class Archivo:
    def __init__(self, nombre, tam, modo, info):
        self.nombre = nombre
        self.tam = tam
        self.modo = modo
        self.info = info
        self.iterador = 0
        self.iteradorImpresion = 0

    #Imprime todos los elementos que hay en la lista y los imprime 
    def dir(archivos):
        for i in range(len(archivos)):
            print(archivos[i].nombre, archivos[i].info," ", end="")
        print("")

    #Verifica que el archivo este cerrado y asigna el modo en el que se le abrio 
    def open(archivo,mode):
        if (archivo.modo == 'C'):
            if(mode == 'W'):
                archivo.info = ""
                archivo.tam = 0
                archivo.modo = 'W'
            elif(mode == 'A'):
                archivo.iterador = len(archivo.info)
                archivo.modo = 'A'
            elif(mode == 'R'):
                archivo.modo = 'R'
            print("Archivo abierto ("+archivo.modo+") -> "+archivo.nombre)
        else:
            print("El archivo ya estaba abierto con un modo, cierralo para poder abrirlo en un nuevo modo")

    #Cierra el archivo cambiando el estado de el mismo a cerrado
    def close(archivo):
        if (archivo.modo != 'C'):
            archivo.modo = 'C'
            archivo.iterador = 0
        else:
            print("El archivo ya estaba cerrado")
    
    #Imprime el contenido del archivo dependiedo del indice que se le pase y la posicion de nuestro iterador
    def read(archivo,indice):
        if(archivo.modo != 'C'):
            if( archivo.modo != 'W'):
                if(indice > archivo.tam):
                    print("El indice sobrepasa la longitud del archivo")
                elif(indice <= archivo.tam):
                    if(archivo.modo=='A'):
                        print(archivo.info[archivo.iteradorImpresion:indice])
                    else:
                        print(archivo.info[archivo.iterador:indice])
            else:
                print("El archivo se ha abierto para escritura, operacion no permitida")
        else:
            print("No se ha abierto el archivo")
    
    #Escribe en el archivo a partir de la posicion en la que se ubique nuestro iterador 
    def write(archivo, textoIngresar, tam):
        if(archivo.modo != 'C'):
            if(archivo.modo != 'R'):
                if(len(textoIngresar) == tam):
                    if tam > 0:
                        auxCad1 = archivo.info[0:archivo.iterador]
                        auxCad2 = archivo.info[archivo.iterador: (archivo.tam)]
                        res = len(auxCad2) - len(textoIngresar)
                        if res > 0:        
                            archivo.info = auxCad1 + textoIngresar + auxCad2[-res:]
                        else:
                            archivo.info = auxCad1 + textoIngresar 
                    else:
                        archivo.info = textoIngresar
                    archivo.tam = len(archivo.info)
                else:
                    print("A ingresado una cadena con un tamaño distinto al dado")
            else:
                print("El archivo esta en modo lectura, operacion no permitida")
        else: 
            print("El archivo no esta abierto")
    
    #Cambia de lugar a ambos iteradores para las operaciones de lectura y escritura 
    def seek(archivo,salto):
        if(archivo.modo != 'C'):
            if(salto > archivo.tam):
                print("El indice sobrepasa la longitud del archivo")
            elif(salto <= archivo.tam):
                if(archivo.modo=='A'):
                    archivo.iteradorImpresion=salto
                    archivo.iterador=salto
                else:
                    archivo.iterador = salto
        else:
            print("El archivo esta cerrado")

#Revisa las entradas para llamar los metodos del archivo en base a su tamaño
def operaComando(lista,archivos):
    tam = len(lista)
    if tam == 1:
        if lista[0] == "dir":
            Archivo.dir(archivos)
        elif lista[0] == "quit":
            return False
        else:
            print("Comando no identificado")

    elif tam == 2:
        if lista[0] == "close":
            for i in range(len(archivos)):
                if archivos[i].nombre == lista[1]:
                    indice = i
            if(type(indice) == type(10)): #
                Archivo.close(archivos[indice])
            else:
                print("No existe el archivo")
        else:
            print("Comando no identificado")

    elif tam == 3:
        indice = False
        for i in range(len(archivos)):
            if archivos[i].nombre == lista[1]:
                indice = i

        if lista[0] == "open":
            if(type(indice) == type(10)): 
                Archivo.open(archivos[indice],lista[2])
            else:
                print("No existe el archivo")
                
        elif lista[0] == "read":
            if(type(indice) == type(10)): 
                try:
                    Archivo.read(archivos[indice],int(lista[2]))
                except: 
                    print("Error ingresando los datos")
            else:
                print("No existe el archivo")
        
        elif lista[0] == "seek":
            if(type(indice) == type(10)): 
                try:
                    Archivo.seek(archivos[indice],int(lista[2]))
                except: 
                    print("Error ingresando los datos")
            else:
                print("No existe el archivo")
        else:
            print("Comando no identificado")
        
    elif tam == 4:
        if lista[0] == "write":
            for i in range(len(archivos)):
                if archivos[i].nombre == lista[1]:
                    indice = i
            if(type(indice) == type(10)): 
                try:
                    Archivo.write(archivos[indice],lista[3],int(lista[2]))
                except: 
                    print("Error ingresando los datos")
            else:
                print("No existe el archivo")
        else:
            print("Comando no identificado")

    else:
        print("Comando no identificado")
        
    return True
#Creacion de archivos
archivos = []
archivos.append(Archivo("A1", 29, "C", "ventadediscosparacomputadoras"))
archivos.append(Archivo("A2", 55, "C", "dsfñadsljfasdkjflsadjfñsafsdafñlsakdjflksadjfwqoieproid"))
archivos.append(Archivo("A3", 16, "C", "43593487jfhhrudg"))
archivos.append(Archivo("A4", 16, "C", "0123456789ABCDEF"))
D_Raiz = Directorio("Raiz", archivos)

#Menu 
print("Intrucciones de la linea de comando para poder implementar el sistema de pseudo-archivos")
print("dir → Muestra el directorio")
print("open <nombreArchivo> <modo> → Especifica que operaremos con el archivo de")
print('                              nombre "nombreArchivo", empleando el modo especificado.')
print("                              Entrega un descriptor de archivo numérico")
print("close <nombreArchivo> → Termina una sesión de trabajo con el archivo")
print("                     referido por el descriptor indicado. Después de un close,")
print("                     cualquier intento por usar ese archivo entregará error.")
print("read <nombreArchivo> <longitud> → Lee la cantidad de bytes especificada")
print('write <nombreArchivo> <longitud> <cadena> → Escribe la cantidad de bytes especificada en el archivo "nombrearchivo"')
print("                                            guardando los datos indicados como parámetro") 
print("seek <nombreArchivo> <posicion> → Salta a la ubicación del archivo en bytes especificada del archivo.")
print("quit → Detiene la ejecución de la terminal")

termina = True
while termina:
    opcion = input("> ")
    aux=opcion.split() #La lectura se separa en un arreglo para saber que operacion hacer
    termina = operaComando(aux, D_Raiz.Archivos)
