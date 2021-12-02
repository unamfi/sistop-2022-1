# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:06:27 2021

@author: RGJG
"""
global A 
global posicion
A=[]
posicion=0
def modos(archivo,identificador,modo,A,posicion):
    A.append([archivo,identificador,modo,posicion,False])
    return A
print("""dir → Muestra el directorio
open <arch> <modo> → Especifica que operaremos con el archivo de
         nombre "arch", empleando el modo especificado. Entrega un
		 descriptor de archivo numérico.
close <descr> → Termina una sesión de trabajo con el archivo
         referido por el descriptor indicado. Después de un close,
		 cualquier intento por usar ese archivo entregará error.
read <descr> <longitud> → Lee la cantidad de bytes especificada
write <descr> <longitud> <datos» → Escribe la cantidad de
         bytes especificada, guardando los datos indicados
		 como parámetro.
seek <descr> <ubicacion> → Salta a la ubicación especificada del
         archivo.
quit → Detiene la ejecución de la simulación
      """)
arch1="También puede escribir una palabra clave para buscar en línea el vídeo que mejor se adapte a su documento.Para otorgar a su documento un aspecto profesional, Word proporciona encabezados, pies de página, páginas de portada y diseños de cuadro de texto que se complementan entre sí."
arch2="El vídeo proporciona una manera eficaz para ayudarle a demostrar el punto. Cuando haga clic en Vídeo en línea, puede pegar el código para insertar del vídeo que desea agregar. También puede escribir una palabra clave para buscar en línea el vídeo que mejor se adapte a su documento.Para otorgar a su documento un aspecto profesional, Word proporciona encabezados, pies de página, páginas de portada y diseños de cuadro de texto que se complementan entre sí."
arch3="440a93fe-45d7-4ccc-a6ee-baf10ce7388a"
directorio = ['arch1 [{}]'.format(str(len(arch1))+" bytes"),'arch2 [{}]'.format(str(len(arch2))+" bytes"),'arch3 [{}]'.format(str(len(arch3))+" bytes")]

while True:
    comando = str(input("→ "))
    comando = comando.split(' ')
    if comando[0] =="dir":
        print('  '.join(directorio))
    elif comando[0] == "open":
            if comando[2]=='R':
                if comando[1]=="arch1":
                    identificador = 1
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                elif comando[1]=="arch2":
                    identificador = 2
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                elif comando[1]=="arch3":
                    identificador = 3
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                else:
                    print('Lo siento, no se puede abrir el archivo {}'.format(comando[3]))
            elif comando[2]=='A':
                if comando[1]=="arch1":
                    identificador = 1
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                elif comando[1]=="arch2":
                    identificador = 2
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                elif comando[1]=="arch3":
                    identificador = 3
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                else:
                    print('Lo siento, no se puede abrir el archivo {}'.format(comando[3]))
            elif comando[2]=='W':
                if comando[1]=="arch1":
                    identificador = 1
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                elif comando[1]=="arch2":
                    identificador = 2
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                elif comando[1]=="arch3":
                    identificador = 3
                    print('Archivo abierto ({}) → {}'.format(comando[2],identificador))
                    A=modos(comando[1],identificador,comando[2],A,posicion)
                else:
                    print('Lo siento, no se puede abrir el archivo {}'.format(comando[3]))
            else:
                print('Error en el modo')
    elif comando[0] == 'read':
        print(A)
        print('Tiene {} archivos'.format(len(A)))
        if comando[1] == '1':
            if A[0][4]==False:
                encontrado = A[0].index(1)
                if A[0][encontrado+1]=='R' or A[0][encontrado+1]=='A':
                    print(arch1[A[0][3]:A[0][3]+int(comando[2])])
                else:
                    print('Accion ilegal')
            else:
                print("Error: el identificador #1 ya está cerrado")
        elif comando[1] == '2':
            if A[1][4]==False:
                encontrado = A[1].index(2)
                if A[1][encontrado+1]=='R' or A[1][encontrado+1]=='A':
                    print(arch2[A[1][3]:A[1][3]+int(comando[2])])
                else:
                    print('Accion ilegal')
            else:
                print("Error: el identificador #2 ya está cerrado")                
        elif comando[1] == '3':    
            if A[2][4]==False:
                encontrado = A[2].index(3)
                if A[2][encontrado+1]=='R' or A[2][encontrado+1]=='A':
                    print(arch3[A[2][3]:A[2][3]+int(comando[2])])
                else:
                    print('Accion ilegal')
            else:
                print("Error: el identificador #1 ya está cerrado")
        else:
            print('ERROR: No tienes permisos de realizar esta accion')
    elif comando[0] == 'seek':
        if comando[1] == '1':    
            if A[0][4]==False:
                encontrado = A[0].index(1)
                if A[0][encontrado+1]=='R' or A[0][encontrado+1]=='A':
                    posicion = int(comando[2])
                    A[0][3]   = posicion  
            else:
                print("Error: El identificador #1 ya está cerrado")
        elif comando[1] == '2':  
            if A[1][4]==False:
                encontrado = A[1].index(2)
                if A[1][encontrado+1]=='R'or A[1][encontrado+1]=='A':
                    posicion = int(comando[2])
                    A[1][3]   = posicion
            else:
                print("Error: El identificador #2 ya está cerrado")
        elif comando[1] == '3':
            if A[2][4]==False:
                encontrado = A[2].index(3)
                if A[2][encontrado+1]=='R' or A[2][encontrado+1]=='A' :
                    posicion = int(comando[2])
                    A[2][3] = posicion
            else:
                print("Error: El identificador #3 ya está cerrado")
        else:
            print('ERROR: No tienes permisos de realizar esta accion')
        print(A)
    elif comando[0] == 'write':
        if comando[1] == '1':
            if A[0][4]==False:
                encontrado = A[0].index(1)
                if A[0][encontrado+1]=='W' or A[0][encontrado+1]=='A':
                    cadenaarem=arch1[posicion:posicion+int(comando[2])+1]
                    arch1 = arch1.replace(cadenaarem,comando[3])
                else:
                    print('Accion ilegal')
            else:
                print("Error: El identificador #1 ya está cerrado")
        elif comando[1] == '2':   
            if A[1][4]==False:
                encontrado = A[1].index(2)
                print("Encontrado en {} y dos posiciones adelantadas esta en modo {}".format(encontrado,A[1][encontrado+1]))
                if A[1][encontrado+1]=='W':
                    cadenaarem=arch2[posicion:posicion+int(comando[2])+1]
                    arch2 = arch2.replace(cadenaarem,comando[3])
                elif A[1][encontrado+1]=='A':
                    cadenaarem=arch2[posicion:posicion+int(comando[2])+1]
                    arch2 = arch2.replace(cadenaarem,comando[3])
                    print('Se modificó con exito')    
                else:
                    print('Accion ilegal')
            else:
                print("Error: El identificador #2 ya está cerrado")
        elif comando[1] == '3': 
            if A[2][4]==False:
                encontrado = A[2].index(3)
                if A[2][encontrado+1]=='W' or A[2][encontrado+1]=='A':
                    cadenaarem=arch3[posicion:posicion+int(comando[2])+1]
                    arch3 = arch3.replace(cadenaarem,comando[3])
                else:
                    print('Accion ilegal')
            else:
                print("Error: El identificador #3 ya está cerrado")
    elif comando[0] == 'close':
        if comando[1] =='1':
            A[0][4] = True            
            print(0)
        elif comando[1] =='2':
            A[1][4]=True
            print(0)
        elif comando[1] =='3':
            A[2][4]=True
            print(0)
    elif comando[0] == 'quit':
        break
    else: 
        print("No hay comando asociado a {}".format(comando))
    
