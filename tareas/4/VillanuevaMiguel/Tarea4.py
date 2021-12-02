import time

class archivo:
    #creación de una clase para guardar los atributos de cada archivo 
    ubicacion=0
    def __init__(self,arch,descr,modo,longitud,datos):
        self.arch=arch
        self.descr=descr
        self.modo=modo
        self.datos=datos
        self.longitud=len(datos)
        
    #Función para simular la apertura de un archivo y otorgar ejecución a las demas funciones
    def abrir():
        print("Abriendo archivo.....")
        time.sleep(2)
        #sacamos del directorio al archivo que necesitamos abrir
        Archivo=dic.get(palabra[1])
        Archivo.modo=palabra[2]
        print("Archivo abierto (",Archivo.modo,") -> ",Archivo.descr )
        
    #Esta función nos ayuda a leer el contenido del archivo
    def read():
        #Sacamos del directorio2 a el archivo solicitado para hacer uso de los atributos necesarios
        Archivo=dic2.get(int(palabra[1])-1)
        leer=Archivo.datos[int(Archivo.ubicacion):int(palabra[2])]
        print("el contenido del archivo es: ",leer)
    
    #Esta función escribe sobre el archivo
    def write():
        Archivo=dic2.get(int(palabra[1])-1)
        #a continuacion y dependiendo del seek veremos si se sobreescribe el archivo o se modifica
        if Archivo.ubicacion == 0:
            Archivo.datos=palabra[3]
            Archivo.longitud=len(palabra[3])
        elif Archivo.ubicacion != 0:
            dato=Archivo.datos
            Esc=Archivo.datos[:int(Archivo.ubicacion)]
            sobree=palabra[3]
            sobree2=len(sobree)
            Esc2=Archivo.datos[int(Archivo.ubicacion)+sobree2:len(dato)]
            largo=sobree2+int(Archivo.ubicacion)
            if len(dato)>= largo:
                Archivo.datos = Esc+sobree+Esc2
            else:
                print("Error: lo que decea escribir sobrepasa el tamaño del archivo")
                
    #nos manda a la ubicacion solicitada para modificar o leer el archivo en una ubicacion especifica
    def seek():
        Archivo=dic2.get(int(palabra[1])-1)
        Archivo.ubicacion=palabra[2]
        
    #Función que deja al archivo en el estado "close"
    def close():
        #print("pos me cierro")
        Archivo=dic2.get(int(palabra[1])-1)
        Archivo.modo="close"
        print ("El archivo se ha cerrado con exito")
    
    #Sirve para generar una impresion donde apareceran los archivos tanto generados como precargados
    def directorio():
        for i in range (len(archivos)):
            impresion=dic2.get(i)
            print(impresion.arch,"[",impresion.longitud,"bytes]")

entrada=0
print("\n==============Bienvenido===============")
#arreglo para meter los nombres de los archivos existentes
archivos=[]
#inicializacion de los objetos que nos serviran como archivos
arch1=archivo("arch1",1, 'close', 9 , "holamundo")
archivos.append(arch1.arch)
otro_mas=archivo("otro_mas",2,'close',6 , "sistop")
archivos.append(otro_mas.arch)
arch2=archivo("arch2",3, 'close', 5,"datos")
archivos.append(arch2.arch)
dic={"arch1":arch1,"otro_mas":otro_mas,"arch2":arch2}
dic2={0:arch1,1:otro_mas,2:arch2}
i=3
ini=0

#genera la "interfas" mientras que nosotros no escribamos quit
while entrada != "quit":
    #solicita y separa palabra por palabra el comando a ejecutar para su uso
    entrada=input("C:\ User> ")
    palabra=entrada.split()
    accion=palabra[0]
    
    #verifica que el comando es open y nos manda a abrir o crear un archivo
    if accion=="open" and len(palabra)==3:
        if palabra[1] in archivos:    
            if palabra[2]=="R" or palabra[2]=="W" or palabra[2]=="A":
                archivo.abrir()
            else:
                print("el modo seleccionado no existe o esta en minusculas")
        else:
            pregunta=input("No existe dicho archivo. ¿decea crear uno con este nombre?")
            if pregunta=="no":
                continue
            #Creación del archivo
            if pregunta=="si":
                cont=i+1
                dato=input("ingrese el contenido del archivo:  ")
                palabra[1]=archivo(palabra[1],cont,palabra[2],len(dato),dato)
                #print(cont)
                archivos.append(palabra[1].arch)
                dic.setdefault(palabra[1].arch,palabra[1])
                num=palabra[1].descr
                dic2.setdefault(num-1,palabra[1])
                i=i+1
                print("Generando archivo........")
                time.sleep(2)
                print("archivo creado con exito")
                
    #Verifica que el comando sea close y ejecuta la funcion close.
    #Si el archivo se encuentra cerrado no modifica su estado
    elif accion=="close" and len(palabra)==2 :
        Archivo=dic2.get(int(palabra[1])-1)
        mod=Archivo.modo
        if mod=="close":
            print("el archivo ya se encuentra cerrado")
        else:
            archivo.close()
            
    #verifica que el comando sea read y ejecuta la funcion read
    elif accion=="read" and len(palabra)==3:
        Archivo=dic2.get(int(palabra[1])-1)
        mod=Archivo.modo
        if mod=="close":
            print("el archivo se encuentra cerrado")
        elif mod =="W":
            print("el archivo solo esta abierto para escritura")
        elif mod=="R" or mod=='A':
            archivo.read()
        elif Archivo not in dic2:
            print("Error: el archivo no existe")
        else:
            print("el archivo no existe o se escribio algo mal")
    
    #verifica que el comando sea write y ejecuta la funcion write
    elif accion=="write" and len(palabra)==4:
        Archivo=dic2.get(int(palabra[1])-1)
        mod=Archivo.modo
        if mod=="close":
            print("el archivo se encuentra cerrado")
        elif mod =="R":
            print("el archivo solo esta abierto para lectura")
        elif mod=="W" or mod=='A':
            archivo.write()
        else:
            print("el archivo no existe o se escribio algo mal")
      
    #verifica que el comando sea seek y ejecuta la funcion seek
    elif accion=="seek" and len(palabra)==3:
        Archivo=dic2.get(int(palabra[1])-1)
        mod=Archivo.modo
        if mod=="close":
            print("el archivo se encuentra cerrado")
        else:
            archivo.seek()
    
    #verifica que el comando sea dir y ejecuta la funcion directorio
    elif accion=="dir":
        archivo.directorio()
            
    #Nos imprime un texta antes de sacarnos de la ejecucion
    elif accion=="quit":
        print("hasta la proxima")
        
    #si llegamos a escribir algun comando erroneo nos va a decir que la opcion es invalida
    else:
        print("opcion invalida")