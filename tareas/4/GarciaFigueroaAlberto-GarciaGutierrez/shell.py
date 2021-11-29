from typing import Sized
import re
import time
#Definimos los atributos de un archivo, así como un método que verifica los permisos que tiene
class Fichero:
    def __init__(self,nombre,size,modo,contenido):
        self.nombre = nombre
        self.size = size
        self.modo = modo
        self.contenido = contenido
        self.ubi_in_file = 0
    def check_mode(self):
        return self.modo



#Esta clase será la encargada de ejecutar los comandos que manipulen archivos
class Shell:
    #Método que abre un archivo, para pasar de cerrado a, por ejemplo, lectura
    def open(file_to_open,fileName,fileMode):
        if(file_to_open.check_mode() != 'C'):
            print('El archivo ya está abierto, deberá de cerrarlo primero')
        else:
            file_to_open.modo = fileMode
            file_to_open.ubi_in_file = 0
            print("Archivo abierto("+str(fileMode)+") -> "+fileName)
            if(file_to_open.modo == 'W'):
                file_to_open.size = 0
                file_to_open.contenido = ''
    #El método close se encarga de cerrar los archivos, ya que de no hacerlo no se podrá ejecutar otra manipulación en el archivo en cuestión
    def close(file_to_close,fileName):
        if(file_to_close.check_mode() != 'C'):
            file_to_close.modo = 'C'
            print("Archivo "+fileName+' cerrado')
        else:
            print('El archivo '+fileName+' ya se encuentra cerrado')
    #El método read sirve para leer el contenido de un archivo, para usarlo se debe habilitar el archivo en modo lectura
    def read(file_to_read,long):
        size=len(file_to_read.contenido)
        
        if(long > size):
            print('La longitud a leer es mayor al tamaño del archivo')
        else:
           print(file_to_read.contenido[0:long])
    #El método write sirve para escribir (y reemplazar por completo) el contenido de un archivo, para usarlo se debe habilitar el archivo en modo escritura
    def write(file_to_write,long,text):
        sizeText=len(text)
        if(long!=sizeText):
            print("La longitud de la cadena ingresada no coincide la longitud declarada")
        else:
            if file_to_write.modo=='W':
                file_to_write.contenido=text
                file_to_write.size=long
            elif file_to_write.modo=='A':
                contenido = file_to_write.contenido
                if(file_to_write.ubi_in_file == 0):
                    file_to_write.contenido=file_to_write.contenido + text
                    file_to_write.size=file_to_write.size+long
                else:
                    contenido= file_to_write.contenido[0:file_to_write.ubi_in_file-1]+text+file_to_write.contenido[file_to_write.ubi_in_file-1+long:]         
                    file_to_write.contenido= contenido
                    file_to_write.size= len(contenido)
                    file_to_write.ubi_in_file=0
    #El método seek permite abrir un archivo (en lectura o escritura) a partir de una ubicación en bytes en específico
    def seek(file_to_seek, ubi):
        file_to_seek.ubi_in_file = int(ubi)
    #El método dir muestra el contenido del directorio   
    def dir(files):
        for i in files:
            print(i.nombre+'['+str(i.size)+' bytes]',end='    ')
        print()
    #El método validar existencia, comprueba la exitencia de un archivo, en caso de que no exista la terminal lo notifica.
    def valida_existencia_file(files,nombre_archivo):
        file_to_open = next((x for x in files if x.nombre == nombre_archivo), None)
        if(file_to_open== None):
            print("El archivo indicado no existe")
        return file_to_open
    #El método validar modo comprueba el modo que reecibe el archivo sea correcto
    def valida_modo(modo):
        if(modo == 'W' or modo == 'R'or modo == 'A'):
            return True
        else:
            print('Privilegios incorrectos'+str(modo)+' no es un modo válido')
            return None





def main():
    files = []
    #Archivos Prueba
    files.append(Fichero("arch1",30,'C','012345678901234567890123456789'))
    files.append(Fichero("arch2",40,'C','0123456789012345678901234567890123456789'))
    files.append(Fichero("arch3",26,'C','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    files.append(Fichero("arch4",50,'C','01234567890123456789012345678901234567890123456789'))
    print("Para poder usar la terminal, se deben respetar los siguientes comandos, ya que de no hacerlo la terminal") 
    print("rechazará el comando")
    print("dir → Muestra el directorio")
    print("open <nombreArchivo> <modo> → Especifica que operaremos con el archivo de")
    print('nombre "nombreArchivo", empleando el modo especificado.')
    print("close <nombreArchivo> → Termina una sesión de trabajo con el archivo")
    print("referido por el descriptor indicado. Después de un close,")
    print("cualquier intento por usar ese archivo entregará error.")
    print("read <nombreArchivo> <longitudBytes> → Lee la cantidad de bytes especificada")
    print("write <nombreArchivo> <longitudBytes> <Cadena> → Escribe la cantidad de")
    print('bytes especificada en el archivo "nombrearchivo", guardando los datos indicados como parámetro "cadena" ')
    print("seek <nombreArchivo> <PosicionBytes> → Salta a la ubicación del archivo en bytes especificada del")
    print("archivo.")
    print("quit → Detiene la ejecución de la terminal")
    print("")
    print("")
    time.sleep(1)
    print("Iniciando la shell chiquita :D")
    time.sleep(1)
    x=True
    while x:
        #Expresiones regulares muy útiles!
        command = input("/: ")
        dir_check=re.search("^dir$",command)
        quit_check=re.search("^quit$",command)
        open_check=re.search("^(open) ([a-zA-Z0-9])+ [A-Za-z]$",command)
        close_check=re.search("^(close) ([a-zA-Z0-9])+$",command)
        read_check=re.search("^(read) ([a-zA-Z0-9])* [0-9]+$",command)
        write_check=re.search("^(write) ([a-zA-Z0-9])* [0-9]+ [A-Za-z0-9!\"\#$%&()=?¿¡!''\{\}\-_.,;:+*]*$",command)
        seek_check=re.search("^(seek) ([a-zA-Z0-9])* [0-9]+$",command)
        
        parametros=re.split("\s", command)
        #Obtenemos los valores que se ingresan por comando 
        try:
            parametro1=parametros[1]
            parametro2=parametros[2]
            parametro3=parametros[3] 
        except IndexError:
            pass
        #Con los siguientes if-else podremos identificar la operación que se tiene que ejecutar en la terminal
        if dir_check!=None:
            Shell.dir(files)
        elif quit_check!=None:
            x=False 
        elif open_check!=None:
            file_to_open = Shell.valida_existencia_file(files,parametro1)
            validador = Shell.valida_modo(parametro2)
            if(file_to_open != None and validador != None):
                Shell.open(file_to_open,parametro1,parametro2)
        elif close_check!=None:
            file_to_close = Shell.valida_existencia_file(files,parametro1)
            Shell.close(file_to_close,parametro1)
        elif read_check!=None:
            file_to_read = Shell.valida_existencia_file(files,parametro1)
            if(file_to_read != None):
                if(file_to_read.modo == 'W' or file_to_read.modo == 'C'):
                    print('El archivo está en modo '+file_to_read.modo)
                else:
                    Shell.read(file_to_open, int(parametro2))
        elif write_check:
            file_to_write = Shell.valida_existencia_file(files,parametro1)
            if(file_to_write != None):
                if(file_to_write.modo == 'R' or file_to_write.modo == 'C'):
                    print('El archivo está en modo '+file_to_write.modo)
                else:
                    Shell.write(file_to_open, int(parametro2),parametro3)
        elif seek_check:
            file_to_seek = Shell.valida_existencia_file(files,parametro1)
            if(file_to_seek != None):
                if(file_to_seek.modo == 'R' or file_to_seek.modo == 'C'):
                    print('El archivo está en modo '+file_to_seek.modo)
                else:
                    Shell.seek(file_to_seek,parametro2)
        else: 
            print("Error, repite por favor")
    print("Cerrando shell...")

main()