from file import File
import re

files = []
descriptores = {}
num_descriptor = 1

def error(id):
    if(id == 1):
        print('El archivo está cerrado')
    elif(id == 2):
        print('El archivo está en modo de lectura')
    elif(id == 3):
        print('El archivo está en modo de escritura')
    elif(id == 4):
        print('El tamaño de la cadena no es el indicado')
    elif(id == 5):
        print('El archivo ya había sido abierto')
    elif(id == 6):
        print('El comando ingresado es inválido')
    elif(id ==7):
        print('Intentaste acceder a una posición mayor al tamaño del archivo')
    elif(id == 8):
        print('El archivo no existe')
    elif(id == 9):
        print('El archivo ya estaba cerrado')
    elif(id == 10):
        print('El descriptor ya está cerrado')

def instructions():
    print('---------------------------------BIENVENIDO--------------------------------------------')
    print('')
    print("Los posibles comandos a emplear son los siguientes:") 
    print("dir → Muestra el directorio")
    print("open <arch> <modo> → Especifica que operaremos con el archivo de")
    print('nombre "arch", empleando el modo especificado. Entrega un')
    print("descriptor de archivo numérico")
    print("close <descr> → Termina una sesión de trabajo con el archivo")
    print("referido por el descriptor indicado. Después de un close,")
    print("cualquier intento por usar ese archivo entregará error.")
    print("read <descr> <longitud> → Lee la cantidad de bytes especificada")
    print("write <descr> <longitud> <datos> → Escribe la cantidad de")
    print('bytes especificada en el archivo "descr", guardando los datos indicados como parámetro')
    print("seek <descr> <ubicación> → Salta a la ubicación del archivo especificada del")
    print("archivo.")
    print("quit → Detiene la ejecución de la simulación")
    print('')

def start():
    global files
    files.append(File("arch1","ABCDEFGHIJ0123456789"))
    files.append(File("arch2","0123456789ABCDE"))
    files.append(File("arch3","ABCDEFGHIJKLMNO0123456789"))
    files.append(File("arch4","0123456789"))

def checkInput():
    line = input('» ')

    dir_regex=re.search("^dir$",line)
    quit_regex=re.search("^quit$",line)
    open_regex=re.search("^open [A-Za-z_][A-Za-z0-9_]* [RWA]$",line)
    close_regex=re.search("^close [0-9]+$",line)
    read_regex=re.search("^read [0-9]+ [0-9]+$",line)
    write_regex=re.search("^write [0-9]+ [0-9]+ .+$",line)
    seek_regex=re.search("^seek [0-9]+ [0-9]+$",line)
    
    if dir_regex != None:
        dir()
        return
    elif quit_regex != None:
        exit()
    
    args = line.split()[1:]

    if open_regex != None:
        open(args[0],args[1])
    elif close_regex != None:
        close(int(args[0]))   
    elif read_regex != None:
        read(int(args[0]),int(args[1]))
    elif write_regex != None:
        write(int(args[0]),int(args[1]),args[2])
    elif seek_regex != None:
        seek(int(args[0]),int(args[1]))
    else:
        error(6)
 
def dir():
    global files
    for i in files:
        print(i.name + " [" + str(i.size) + " bytes]" )

def open(filename, mode):
    global num_descriptor, descriptores, files
    #Obtener el archivo correspondiente al nombre
    file = None
    for i in files:
        if i.name == filename: file = i
    if file is None:
        error(8)
        return

    #Revisar si el archivo ya estaba abierto
    if(file.isOpen()):
        error(5)
        return
    
    #Revisar si el modo del archivo es válido
    opened = file.open(mode)
    if(opened == -1):
        error(6)
    else:
        descriptores[num_descriptor] = file
        print("Archivo abierto (" + str(file.mode) + ") -> " + str(num_descriptor))
        num_descriptor = num_descriptor + 1
        


def close(num):
    file = getFile(num)
    if file is None: 
        error(10)
        return
    #Revisar si el archivo ya estaba cerrado        
    if(file.isOpen):
        file.close()
        descriptores.pop(num)
    else:
        error(9)


def getFile(num):
    global descriptores
    file = descriptores.get(num)
    return file

def read(num, length):
    file = getFile(num)
    if file is None: 
        error(10)
        return
    #Revisar si está en el modo correcto
    result = file.read(length)
    if(result == -1):
        error(3)
    else:
        #Revisar si se la posición solicitada está en los límites
        if(file.pointer + length > file.size):
            error(7)
            return
        print(result)     

def write(num , length, data):
    file = getFile(num)
    if file is None: 
        error(10)
        return
    #Revisar si la longitud declarada coincide con la real
    if(length != len(data)):
        error(4)
        return

    #Revisar si está en el modo correcto
    result = file.write(data)
    if(result == -1):
        error(3)

def seek(num, place):
    file = getFile(num)
    if file is None: 
        error(10)
        return    
    #Revisar si se la posición solicitada está en los límites
    result = file.movePointer(place)
    if(result == -1):
        error(7)



instructions()
start()
while True:
    checkInput()