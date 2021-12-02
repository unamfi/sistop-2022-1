# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:43:13 2021

@author: Carlo
"""

class Archivo: #Clase para erificar archivos precargados
    def __init__(self,nombre,contenido,estado):
        self.nombre=nombre
        self.contenido=contenido
        self.longitud=len(contenido)
        self.estado=estado
class Open: #Clase para crear y/ abrir archivos
    def __init__(self,nombre,contenido,estado1,descriptor):
        self.nombre=nombre
        self.contenido=contenido
        self.estado1=estado1
        self.descriptor=descriptor
    def lectura(nombre,n): #R Lectura
        print("Archivo ",nombre, "(R) ->",n)
        pass
    def escritura(nombre,n): #W Escritura
        print("Archivo ",nombre ,"(W) ->",n)
        pass
    def modificar(nombre,n): #A Modificar
        print("Archivo ",nombre ,"(A) ->",n)
        pass
def impresionDir(nombreArchivos): #Imprimir los archivos que estan
    for obj in nombreArchivos:
        print("\t",obj.nombre,int( len(obj.contenido)*10.24),"[bytes]")
def verificarCerrado(abiertos,nombreCerrado): #Verificador que el archivo este cerrado
    for objBuscar in abiertos:
        if objBuscar.nombre==nombreCerrado:
            continue
    print("El archivo ya se encuentra cerrado o no existe")
def estado(nombre,tipo,n): #Impresion de l tipo de estado : R,W,A
    estado1=str(tipo)
    if estado1=="W":
        Open.escritura(nombre,n)
    elif estado1=="R":
        Open.lectura(nombre,n)
    elif estado1=="A":
        Open.modificar(nombre,n)
    else:
        print("No existe ese modo")
def read(archivos,num,numCaracter):#Funcion que permite leer archivos con R o A
    for objNum in archivos:
        if objNum.descriptor==int(num):
            nombre=objNum.nombre
            for objModo in archivos:
                if objModo.nombre==nombre:
                    if objModo.estado1=="R" or objModo.estado1=="A":
                        #print("Se puede leer")
                        caracteres=objModo.contenido[:int(numCaracter)]
                        #print("Los caracteres son de longitud ",len(objModo.contenido))
                        #print(objModo.contenido)
                        print(caracteres)
                    else:
                       print("Error: El archivo",nombre,"no se puede escribir por que es modo ", objModo.estado1)
                        
                        
   #Verificador que indica que existe o no dicho archivo, asi como el descriptor
    if len(archivos)==0:
        verificar=False
    else:
        for objVer in archivos:
            if objVer.descriptor==int(num):
                verificar=True
                break
            else:
                verificar=False
    if verificar==False:
        print("Error: no existe ese documento o esta cerrado con el descriptor num ",num)
       
ubicacion=[]
caracter=[]
def seek(archivos,num,posicion):#Funcion para seek 
    caracter.clear()
    ubicacion.clear()
    for objDes in archivos:
        if objDes.descriptor==int(num):
            nombre=objDes.nombre
            for objeNombre in archivos:
                if objeNombre.nombre==nombre:
                    if objeNombre.descriptor==int(num):
                        indices=objeNombre.contenido
                        for i in indices:
                            caracter.append(i)
                        try:
                            for j in range(0,len(caracter)):#Buscar la letra e indice de la posicion indica
                                if j==int(posicion)-1:
                                    indice=j+1
                                    ubicacion.append(indice)#caracter.index(letra)+1)
                                    print(ubicacion)
                                    
                        except: 
                            print("No se encuentra esa localidad")
                        
    #Verificador que indica que existe o no dicho archivo, asi como el descriptor                    
    verificar=True
    if len(archivos)==0:
        verificar=False
    else:
        for objVer in archivos:
            if objVer.descriptor==int(num):
                verificar=True
                break
            else:
                verificar=False
    if verificar==False:
        print("Error: no existe ese documento o esta cerrado con el descriptor num ",num)
    pass

def write(archivos,descriptor,longitud,dato,lugar):#Funcion para write, poder escribir en el archivo
    if len(archivos)==0: #Verificador que indica que existe o no dicho archivo, asi como el descriptor
        verificar=False
    else:
        for objVer in archivos:
            if objVer.descriptor==int(descriptor):
                verificar=True
                break
            else:
                verificar=False
        if verificar==False:
            print("Error: no existe ese documento o esta cerrado con el descriptor num ",descriptor)
        
    for objNum in archivos:
        if objNum.descriptor==int(descriptor):
            nombre=objNum.nombre
            for objModo in archivos:
                if objModo.nombre==nombre:
                    if objModo.estado1=="W" or objModo.estado1=="A":
                         try:
                             if objModo.contenido=="":
                                 nuevo=dato.split()
                                 print("".join(nuevo))
                             else:
                            #print("Se puede escribir")
                                inicio=caracter[:ubicacion[0]-1]
                                palabraNuevo=int(longitud)
                                final=caracter[ubicacion[0]-1+palabraNuevo:]
        
                                nuevo=inicio+dato.split()+final
                                union="".join(nuevo)
                                print(union)
                         except:
                            print("Error: La longitud de la cadena no es la adecuada")
                            
                        
                    else:
                        print("Error: El archivo",nombre,"no se puede escribir por que es modo ", objModo.estado1)
                        
                    
abierto=[]
def verificador(nombre,modo,lista,n,existe):#Funcion para verificar si existe o no el archivo
    #abierto=[]
    for  objeto in lista:
        if objeto.nombre==nombre:
            #print("Ya existe")
            archivoAbierto=Open(objeto.nombre,objeto.contenido,modo,n)#archivoAbierto=Open(objeto.nombre,objeto.contenido,modo,n)
            abierto.append(archivoAbierto)
            estado(objeto.nombre,modo,n)
            existe=True
            break
        else:
            existe=False
    return existe            
print("Users\PavilionHP\Documentos\Sistop-2022-1\Tareas\4") 
archivo=[]
archivo1=Archivo("Tarea1","Hola",None)#Archivo precargados
archivo2=Archivo("Tarea2","SistemasOperativo",None)
archivo3=Archivo("Tarea3","Gol",None)
archivo.append(archivo1)
archivo.append(archivo2)
archivo.append(archivo3)
existe=True
instruccion=0
n=0
while instruccion !="quit":
    instruccion=input(str())
    linea=instruccion.split()
    if linea[0]=="open":
            n +=1
            existencia=verificador(linea[1],linea[2],archivo,n,existe)
            #print("El archivo existe")
            #print(nombre, " abierto",(modo),"->")
            if existencia==False:# Crear nuevo archivo
                contenido=str(input("\tIngrese el contenido del archivo: "))
                archivoNuevo=Open(linea[1],contenido,linea[2],n)#Archivo
                archivo.append(archivoNuevo)
                abierto.append(archivoNuevo)
                estado(linea[1],linea[2],n)
                #openArchivo()
            for objAbierto in abierto:#Comprobar si esta abierto el archivo
                if objAbierto.nombre ==linea[1]:
                    print("Ya esta abierto")
            #break
    elif linea[0]=="close":
        for objCerrado in abierto:#Borrar el archivo de los archivos abiertos
            if objCerrado.descriptor==int(linea[1]):#objAbierto.nombre1 ==linea[1]
                abierto.remove(objCerrado)
                print("cerrado el archivo")
        verificarCerrado(abierto, linea[1])
    elif linea[0]=="dir":
           impresionDir(archivo)
    elif linea[0]=="read":
            read(abierto,linea[1],linea[2])
    elif linea[0]=="write":
           write(abierto,linea[1],linea[2],linea[3],ubicacion)
    elif linea[0]=="seek":
           seek(abierto,linea[1],linea[2])
    elif linea[0]=="quit":
        print("Adios")
    else:
        print("comando equivocado")