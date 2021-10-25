# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 14:24:09 2021

@author: Carlo
"""

#Problema Centro de llamadas telefonicas
#Se considera que son el horario de dicho centro es nocturno
#Por lo cual son hay disponibilidad de 10 telefonos
from threading import Barrier,Thread,Semaphore
import random
import time


def ingresos(num):
    global llamadas,mut_ingreso,max_telefonos,ayuda,servicios,nuevoIngt,telefonos,llamadasEntrante
    while True:
        llamadasEntrante.acquire()
        
        
        #mut_ingreso.release()
        mut_ingreso.acquire() #nuevoIngt.acquire() 
        #numllamadas.append(1)
        print("Sonando el telefono, Rinrinrin")
        time.sleep(10)#Disminuir como a 1 o 2 
        print("Llegando la llamada")
        #telefonos.append(1)
        time.sleep(10)
        mut_ingreso.release()#nuevoIngt.release()
        mut_ingreso.acquire()#nuevoIngt.acquire() #mut_ingreso.acquire() 
        print("Atendiendo una llamada en el telefono num.",num-1)
        telefonos.append(1)
        time.sleep(5)
        #mut_ingreso.acquire()
        mut_ingreso.release()
        llamadasEntrante.release()
        #nuevoIngt.release()
        #nuevoIngt.acquire()
        mut_ingreso.acquire()
        print("Los telefonos ocupados")
        #telefonos.append(1)
        time.sleep(10)
        mut_ingreso.release()
        #nuevoIngt.release()
        #mut_ingreso.acquire()
       
        mut_ingreso.acquire()
        #telefonos.append(1)
        print("Se tienen atendiendo ",max_ingreso.n_waiting+1, "llamadas en este momento")#NOs da el numero de hilos
        print("telefonos hilos ",len(telefonos))
        time.sleep(5)
        mut_ingreso.release()
        max_ingreso.wait()
       # if len(telefonos)==10:
        #    mut_ingreso.acquire()
         #   print("Llamadas en espera, por el momento no se puede atender mas")#llamadas
          #  time.sleep(2)
           # del telefonos[:]# time.sleep(2)
            #print("Por ahora no tenemos llamadas", llamadas)
            #time.sleep(3)
            #mut_ingreso.release()
        #nuevoIngt.acquire()
        #mut_ingreso.acquire()
        #print("Terminando de atender, libre el telefono num.",num)
        #time.sleep(random.randint(2,8))
        #nuevoIngt.release()
        #mut_ingreso.release()
        #max_ingreso.wait()

            

            #max_ingreso.wait()
        #Thread(target=egreso,args=[]).start()

def saturacion():
    global mut_ingreso
    mut_ingreso.acquire()
    print("Llamadas en espera, por el momento no se puede atender mas")#llamadas
    time.sleep(4)
    del telefonos[:]
   # time.sleep(2)
    print("Por ahora no tenemos llamadas", llamadas)
    time.sleep(3)
    mut_ingreso.release()
def egreso(num):#Idea, cambiar lo de egreso por lo de policia, bombero o ambulancia
    global nuevoEgr,mut_egreso,ayuda,mut_ingreso
    while True:
        #nuevoEgr.acquire() Se cambio a mut_egreso
        mut_ingreso.acquire()
        if ayuda==random.randint(3,7):
             #mut_ingreso.acquire()
             mut_egreso.acquire()
             print("Llamando a ",random.choice(servicios))
             time.sleep(3)
             mut_egreso.release()
             #mut_egreso.acquire()
             #print("Va en camnino, a rescate")
             #time.sleep(3)
             # mut_egreso.release()
             #mut_ingreso.release()
        mut_ingreso.release()
        mut_egreso.acquire()
        print("Todo listo, atendiendo")
        time.sleep(random.randint(5,7))
        mut_egreso.release()
        '''nuevoEgr.acquire()
        time.sleep(5)
        nuevoEgr.release()
        print("Esperando una llamada")
        mut_egreso.release()
        print("Sonando el telefono, Riririn")
        mut_egreso.acquire()
        #nuevoEgr.release()
        time.sleep(10)
        #print("Atendiendo la llamada ",llamadas)'''

    #print("Terminando de atender, libre el telefono num.",num)
     #   time.sleep(random.randint(2,8))
        

def main():
    global llamadasEntrante, mut_ocupa
    while True:
        #mut_ingreso.acquire()
        telefonosDisp=10-len(telefonos)
        print("Los telefonos disponibles son ",telefonosDisp)
        print("Telefonos ", telefonos, "longitud ", len(telefonos))
       # print(telefonosDisp)
        if len(telefonos)==10:
            mut_ocupa.acquire()
            print("No hay disponibilidad", telefonos)
            time.sleep(10)
           # print("Se tienen atendiendo ",max_ingreso.n_waiting, "llamadas en este momento")#NOs da el numero de hilos
            #time.sleep(5)
            #mut_ingreso.release()
            #max_ingreso.wait()
            
        else:
            #nuevoIngt.acquire()
            #telefonos.append(1)
            mut_ocupa.release()
            nuevoIngt.release()
            llamadasEntrante.release()
            print("Esperando llamada")
            time.sleep(5)
        #llamadasEntrante.release()
        #print("Sonando el telefono, Rinrinrin")
        #llamadasEntrante.acquire
        #mut_ingreso.release()
        parametros=random.randint(11, 15)
        for num_llamadas in range(1,parametros):
            Thread(target=ingresos,args=[num_llamadas]).start()
        for num_Egreso in range(1,parametros):
            Thread(target=egreso,args=[num_Egreso]).start()

ayuda=5
max_telefonos=10
mut_ocupa=Semaphore(1)
llamadasEntrante=Semaphore(0)
nuevoIngt=Semaphore(0) #No se esta usando
nuevoEgr=Semaphore(1)
mut_egreso=Semaphore(1)#Movi de 0 a 1, problema solo da numero 1
mut_ingreso=Semaphore(1)
max_ingreso=Barrier(9,saturacion)
servicios=["Policias","Bomberos","Ambulancia"]
numllamadas=[]
llamadas=[]
telefonos=[]
Thread(target=main,args=[]).start()
'''Formar una lista de telefonos para ver si hay disponibilidad
con 10 telefonos, remplazando con 1 para ver disponibilidad de telefonos con 
base a la funcion de ingreso, segundo avance poner color a la impresion'''