from typing import Sized
import re
import time

#Expresiones regulares:
# ^(open) ([a-zA-Z0-9])+ (R|W|A)$
# ^(close) ([a-zA-Z0-9])+$
# ^(read) ([a-zA-Z0-9])* [0-9]+$
# ^(write) ([a-zA-Z0-9])* [0-9]+ [A-Za-z0-9!"#$%&()=?¿¡!''{}\-_.,;:+*]*$
# ^(seek) ([a-zA-Z0-9])* [0-9]+$
# ^dir$
# ^quit$

class Fichero:
    def __init__(self,nombre,size,modo,contenido):
        self.nombre = nombre
        self.size = size
        self.modo = modo
        self.contenido = contenido

    def check_mode(self):
        return self.modo




class Shell:
    def open(file_to_open,fileName,fileMode):
        if(file_to_open.check_mode() != 'C'):
            print('El archivo ya está abierto, deberá de cerrarlo primero')
        else:
            file_to_open.modo = fileMode
            print("Archivo abierto("+str(fileMode)+") -> "+fileName)
            if(file_to_open.modo == 'W'):
                file_to_open.size = 0
                file_to_open.contenido = ''
    def close(file_to_close,fileName):
        if(file_to_close.check_mode() != 'C'):
            file_to_close.modo = 'C'
            print("Archivo "+fileName+' cerrado')
        else:
            print('El archivo '+fileName+' ya se encuenrta cerrado')
            
    def read(file_to_read,long):
        size=len(file_to_read.contenido)
        
        if(long > size):
            print('La longitud a leer es mayor al tamaño del archivo')
        else:
           print(file_to_read.contenido[0:long])
    def write(file_to_write,long,text):
        sizeText=len(text)
        if(long!=sizeText):
            print("La longitud de la cadena ingresada no coincide la longitud declarada")
        else:
            if file_to_write.modo=='W':
                file_to_write.contenido=text
                file_to_write.size=long
            elif file_to_write.modo=='A':
                file_to_write.contenido=file_to_write.contenido + text
                file_to_write.size=file_to_write.size+long
    def seek(arch, ubi):
        print("XD")
        
    def dir(files):
        for i in files:
            print(i.nombre+'['+str(i.size)+' bytes]',end='    ')
        print()

    def valida_arch(files,nombre_archivo):
        file_to_open = next((x for x in files if x.nombre == nombre_archivo), None)
        if(file_to_open== None):
            print("EL ARCHIVO NO EXISTE BRO")
        return file_to_open
    def valida_modo(modo):
        if(modo == 'W' or modo == 'R'or modo == 'A'):
            return True
        else:
            print('MODO INCORRECTO')
            return None





def main():
    files = []

    files.append(Fichero("arch1",30,'C','012345678901234567890123456789'))
    files.append(Fichero("arch2",40,'C','0123456789012345678901234567890123456789'))
    files.append(Fichero("arch3",30,'C','012345678901234567890123456789'))
    files.append(Fichero("arch4",30,'C','012345678901234567890123456789'))
    print("Iniciando la shell chiquita :D")
    time.sleep(2)
    x=True
    while x:
        command = input("/:")
        result1=re.search("^dir$",command)
        result2=re.search("^quit$",command)
        result3=re.search("^(open) ([a-zA-Z0-9])+ [A-Za-z]$",command)
        result4=re.search("^(close) ([a-zA-Z0-9])+$",command)
        result5=re.search("^(read) ([a-zA-Z0-9])* [0-9]+$",command)
        result6=re.search("^(write) ([a-zA-Z0-9])* [0-9]+ [A-Za-z0-9!\"\#$%&()=?¿¡!''\{\}\-_.,;:+*]*$",command)
        
        parametros=re.split("\s", command)
        try:
            parametro1=parametros[1]
            parametro2=parametros[2]
            parametro3=parametros[3] 
        except IndexError:
            pass

        if result1!=None:
            Shell.dir(files)
        elif result2!=None:
            x=False 
        elif result3!=None:
            file_to_open = Shell.valida_arch(files,parametro1)
            validador = Shell.valida_modo(parametro2)
            if(file_to_open != None and validador != None):
                Shell.open(file_to_open,parametro1,parametro2)
        elif result4!=None:
            file_to_close = Shell.valida_arch(files,parametro1)
            Shell.close(file_to_close,parametro1)
        elif result5!=None:
            file_to_read = Shell.valida_arch(files,parametro1)
            if(file_to_read != None):
                if(file_to_read.modo == 'W' or file_to_read.modo == 'C'):
                    print('El archivo está en modo '+file_to_read.modo)
                else:
                    Shell.read(file_to_open, int(parametro2))
        elif result6:
            file_to_write = Shell.valida_arch(files,parametro1)
            if(file_to_write != None):
                if(file_to_write.modo == 'R' or file_to_write.modo == 'C'):
                    print('El archivo está en modo '+file_to_write.modo)
                else:
                    Shell.write(file_to_open, int(parametro2),parametro3)
        else: 
            print("No te entendi un carajo, repite por favor")
    print("Cerrando shell...")

main()