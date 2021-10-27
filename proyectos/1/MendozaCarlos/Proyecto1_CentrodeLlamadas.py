#@author: Carlos Mendoza
#Problema Centro de llamadas telefonicas HELP
#Se considera que un promedio de 10 telefonos en uso por hora
#Por lo cual son hay disponibilidad de 10 telefonos

#Uso de las bibliotecas Threading para el manejo de los hilos, random para el uso del azar 
#y time para el uso del tiempo
from threading import Barrier,Thread,Semaphore
import random
import time

#Funcion ingreso donde ingresa los hilos (llamadas) en cual se lleva el registro
#Asi como la frecuencia revision de los telefonos disponibles
def ingresos(num):
    global mut_ingreso,telefonos,llamadasEntrante #Variables globales a ocupar
    while True:
        llamadasEntrante.acquire()
        mut_ingreso.acquire() 
        print("  Sonando el telefono, Rinrinrin")
        time.sleep(3)
        print("Llegando la llamada")
        time.sleep(3)
        mut_ingreso.release()
        mut_ingreso.acquire()
        print("Atendiendo una llamada en el telefono num.",num)
        telefonos.append(1)
        time.sleep(5)
        mut_ingreso.release()
        #llamadasEntrante.release()
        mut_ingreso.acquire()
        print("Los telefonos ocupados")
        time.sleep(10)
        mut_ingreso.release()
        mut_ingreso.acquire()
        print("Se tienen atendiendo ",max_ingreso.n_waiting+1, "llamadas en este momento")#NOs da el numero de hilos
        print("Telefonos ocupados son",len(telefonos))
        time.sleep(5)
        mut_ingreso.release()
        llamadasEntrante.release()
        max_ingreso.wait()#Barrera que espera 10 hilos, teniendo en cuenta la restriccion
        if len(telefonos)==10:
            mut_ingreso.acquire()
            print("Llamadas en espera, se espera terminar la llamada en los telefonos")
            time.sleep(3)
            del telefonos[:]
            print("Por ahora no tenemos llamadas",telefonos, "se liberon los telefonos ")
            time.sleep(3)
            mut_ingreso.release()
       

#Funcion en cual se lleva acabo la solicitud del servicio o todavia seguir atendiendo la llamada
#En funcion de los hilos entrantes 
def egreso(num):
    global mut_egreso,ayuda,mut_ingreso
    while True:
        
        mut_ingreso.acquire()
        if ayuda==random.randint(3,7):#Probabilidad aleatoria para solicitar un servicio
             #mut_ingreso.acquire()
             mut_egreso.acquire()
             print("Llamando a" ,str(random.choice(servicios)))
             print("Va en camino, a rescate")
             time.sleep(3)
             mut_egreso.release()
             
        llamadasEntrante.release()
        mut_ingreso.release()
        mut_egreso.acquire()
        print("  Se sigue atendiendo la llamada entrante ")
        time.sleep(random.randint(4,7))
        mut_egreso.release()
        llamadasEntrante.acquire()
        
        
#Hilo Main en donde se llamara los hilos de llamadas, en funcion de ingreso y egreso
#Asi como la comparacion de la disponibilidad de los telefonos
def main():
    global llamadasEntrante, mut_ocupa #Variables globales a usar
    while True:
        #mut_ingreso.acquire()
        telefonosDisp=10-len(telefonos)#
        print("Los telefonos disponibles son ",telefonosDisp)
        print("Telefonos ", telefonos, "ocupados ", len(telefonos))#Representacion de 1, que indica como se va ocupando los telefonos
        mut_ocupa.release()
        nuevoIngt.release()
        llamadasEntrante.release()
        print("Esperando llamada")
        time.sleep(5)
        parametros=random.randint(11, 15)
        for num_llamadas in range(1,parametros):
            Thread(target=ingresos,args=[num_llamadas]).start()
        for num_Egreso in range(1,parametros):
            Thread(target=egreso,args=[num_Egreso]).start()

#Nuestra variables que seran usadas durante el prograama
#Ayuda es la probabilidad definada para llamar a los servicios
ayuda=5

#Semaforos y mutex que se le asigna a los hilos, dando la fluidez del programa
mut_ocupa=Semaphore(1)
llamadasEntrante=Semaphore(0)
nuevoIngt=Semaphore(0) 
mut_egreso=Semaphore(1)
mut_ingreso=Semaphore(1)

#Barrera que detendra 10 hilos, limite que se tiene considerado 
max_ingreso=Barrier(10)

#Lista de servicios que se brinda
servicios=["Policias","Bomberos","Ambulancia"]

#Lista donde nos inidcara la disponibilidad y el uso de los telefonos
telefonos=[] 
Thread(target=main,args=[]).start()