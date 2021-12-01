class Archivo:
    
    def __init__(self, nombre, modo, descriptor, contenido,aqui):
        self.nombre = nombre
        self.modo = modo
        self.descriptor = descriptor
        self.contenido = contenido
        #'aqui' indicará la posición de dónde se va a leer o escribir
        self.aqui = aqui
        
    def opena(self, modo_apertura,archivos_abiertos,descr):
        self.modo = modo_apertura
        self.descriptor = descr
        print('Archivo abierto (',self.modo,') -> ',self.descriptor)
        archivos_abiertos.setdefault(str(self.descriptor),self)
        #Si el archivo se abre en modo lectura, se descarta su contenido
        #También se establece su tamaño como 0
        if self.modo == 'W':
            self.contenido.clear()
            self.aqui = 0
        return archivos_abiertos
    
    def close(self,cadena3,archivos_abiertos):
        self.modo = 'C'
        archivos_abiertos.pop(cadena3)
        return archivos_abiertos
        
    def read(self,cadena2,cadena3):
        cadena_devuelta =''
        modoap = str(self.modo)
        if modoap=='R' or modoap=='A':
            cadena3 = int(cadena3)
            cadena_devuelta = self.contenido[self.aqui:self.aqui+cadena3]
            cadena_devuelta = ''.join(cadena_devuelta)
            tamaño_cadena = len(cadena_devuelta)-cadena3
            # Verificamos que la longitud pedida no rebase el largo del archivo
            #La verificación se hace a partir de a dónde apunta 'aqui'
            if tamaño_cadena >= 0:
                print(cadena_devuelta)
                cadena3 = str(cadena3)
            else:
                print('Error: la longitud dada, es mayor al contenido del archivo')
        else:
            print('El archivo no se encuentra en modo Lectura o Modificación')
        
    def write(self,cadena2,cadena4,cadena3):
        cadena4 = int(cadena4)
        if self.modo == 'R':
            print('Error: el archivo',self.nombre,' está abierto sólo en modo lectura.')
        if self.modo == 'W' or self.modo == 'A':
            if cadena4 == len(cadena3):
                if self.contenido != []:
                    k = self.aqui
                    for caracter in cadena3:
                        self.contenido.insert(k,caracter)
                        #Se verifica que 'aqui' no apunte al final de la lista
                        if k != len(self.contenido)-1:
                            self.contenido.pop(k+1)
                        k = k+1
                else:
                    #Si 'aqui' apunta al final de la lista
                    #Se escribe directamente al final de la lista
                    k = self.aqui
                    for caracter in cadena3:
                        self.contenido.insert(k,caracter)
                        k = k+1
            else:
                print('Error: la longitud no coincide con el dato')
    
    def seek(self, cadena3):
        cadena3 = int(cadena3)
        if cadena3 <= len(self.contenido) and cadena3 >= 0:
            self.aqui = cadena3
        else:
            print('Error: la ubicación no existe dentro del archivo')
            
def terminal(archivos):
    cadena = ''
    nombre_archivo = ''
    descr = 0
    archivos_abiertos = {}
    while True:
        
        n=0
        m=0
        cadena1 = []
        cadena2 = []
        cadena3 = []
        cadena4 = []
        cadena = input('user/tarea4 $ ')
        
        if cadena == 'dir':
            for key in archivos:
                archivo = archivos.get(key)
                contenido = archivo.contenido
                tamaño = len(contenido)
                print(key,'[',tamaño,'bytes]')
            continue
        
        if cadena == 'quit':
            break
        
        cadena = list(cadena)
        
        #Aquí se separa en listas la entrada del usuario
        for i in range(len(cadena)):
            if cadena[i].isspace() and n==0:
                cadena1.append(cadena[:i])
                n = n+1
                m = i
                continue
            if cadena[i].isspace() and n==1:
                cadena2.append(cadena[m+1:i])
                n = n+1
                m = i
                continue
            if i==len(cadena)-1:
                cadena3.append(cadena[m+1:])
                n = n+1
                m = i
                continue
            if cadena[i].isspace() and n==2:
                cadena4.append(cadena[m+1:i])
                n = n+1
                m = i
                continue
        
        if cadena1 != []:
            cadena1 = ''.join(cadena1[0])
        if cadena2 != []:
            cadena2 = ''.join(cadena2[0])
        if cadena3 != []:
            cadena3 = ''.join(cadena3[0])
        if cadena4 != []:
            cadena4 = ''.join(cadena4[0])

        if cadena1 == 'open':
            if cadena2 != []:
                archivo = archivos.get(cadena2)        
                if cadena2 in archivos:
                    modoa = archivo.modo
                    #Se verifica que el archivo tiene cualquiera de los 3 modos
                    if modoa != 'C':
                        print('El archivo ya se encuentra abierto')
                    elif cadena3 == 'R' or cadena3=='W' or cadena3=='A':
                        print('Abriendo el archivo: ',cadena2)
                        descr = descr + 1
                        archivo.opena(cadena3,archivos_abiertos,descr)
                    else:
                        print('Error: el modo de apertura no es correcto')
                else:
                    print('El archivo no existe')
            else:
                print('Error: comando inválido')
        
        elif cadena1 == 'close':
            if cadena3 in archivos_abiertos:
                archivo = archivos_abiertos.get(cadena3)
                archivo.close(cadena3,archivos_abiertos)
            else:
                print('El archivo no se encuentra abierto o no existe')
                
        elif cadena1 == 'read':
            if cadena2 in archivos_abiertos:
                archivo = archivos_abiertos.get(cadena2)
                archivo.read(cadena2,cadena3)
            else:
                print('El archivo no se encuentra')
                
        elif cadena1 == 'write':
            if cadena2 in archivos_abiertos:
                archivo = archivos_abiertos.get(cadena2)
                archivo.write(cadena2,cadena4,cadena3)
            else:
                print('El archivo no se encuentra abierto')
        
        elif cadena1 == 'seek':
            if cadena2 in archivos_abiertos:
                archivo = archivos_abiertos.get(cadena2)
                archivo.seek(cadena3)
            else:
                print('El archivo no se encuentra abierto')
        
        elif cadena1 == 'crear':
            if cadena3 not in archivos:
                nombre_archivo = Archivo(cadena3,'C',descr,[],0)
                archivos.setdefault(cadena3,nombre_archivo)
            elif cadena3 in archivos:
                print('El archivo ya existe')
        
        else:
            print('Error: comando inválido')

                
def main():
    archivos = {}
    #Se crean los archivos predefinidos
    arch1 = Archivo('arch1','C',1,['h','o','l','a','1'],0)
    archivos.setdefault(arch1.nombre,arch1)
    otro_mas = Archivo('otro_mas','C',1,['h','o','l','a','3','p','r','u','e','b','a'],0)
    archivos.setdefault(otro_mas.nombre,otro_mas)
    arch2 = Archivo('arch2','C',2,['h','o','l','a','2'],0)
    archivos.setdefault(arch2.nombre,arch2)
        
    terminal(archivos)
    
main()