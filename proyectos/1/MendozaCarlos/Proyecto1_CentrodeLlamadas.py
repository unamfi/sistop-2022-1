#Problema Centro de llamadas telefonicas
#Se considera que son el horario de dicho centro es nocturno
#Por lo cual son hay disponibilidad de 10 telefonos
from threading import Barrier,Thread,Semaphore
import random
import time


def ingresos(num):
    global llamadas,mut_ingreso,max_telefonos,ayuda,servicios,nuevoIngt,telefonos,llamadasEntrante
    while True:
       # llamadasEntrante.acquire()
        
        
        #mut_ingreso.release()
        mut_ingreso.acquire() #nuevoIngt.acquire() 
        #numllamadas.append(1)
        print("Sonando el telefono, Rinrinrin")
        time.sleep(10)
        print("Llegando la llamada")
        telefonos.append(1)
        time.sleep(5)
        mut_ingreso.release()#nuevoIngt.release()
        mut_ingreso.acquire()#nuevoIngt.acquire() #mut_ingreso.acquire() 
        print("Atendiendo una llamada en el telefono num.",num)
        time.sleep(5)
        #mut_ingreso.acquire()
        mut_ingreso.release()
        llamadasEntrante.release()
        #nuevoIngt.release()
        #nuevoIngt.acquire()
        mut_ingreso.acquire()
        print("Los telefonos ocupados")
        #telefonos.append(1)
        time.sleep(5)
        mut_ingreso.release()
        #nuevoIngt.release()
        #mut_ingreso.acquire()
        if ayuda==random.randint(2,8):
             mut_ingreso.acquire()
             print("Llamando a ",random.choice(servicios))
             time.sleep(5)
             mut_ingreso.release()
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
    print("Llamadas en espera, por el momento no se puede atender mas")#llamadas
    del llamadas[:]
    time.sleep(10)
    print("Por ahora no tenemos llamadas", llamadas)
def egreso(num):
    global nuevoEgr,mut_egreso
    while True:
        nuevoEgr.acquire()
        print("Terminando de atender, libre el telefono num.",num)
        time.sleep(random.randint(3,8))
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
        telefonosDisp=10-len(telefonos)
        print("Los telefonos disponibles son ",telefonosDisp)
        print("Telefonos ", telefonos, "longitud ", len(telefonos))
       # print(telefonosDisp)
        if len(telefonos)==10:
            mut_ocupa.acquire()
            print("No hay disponibilidad", telefonos)
            time.sleep(10)
            print("Se tienen atendiendo ",max_ingreso.n_waiting, "llamadas en este momento")#NOs da el numero de hilos
            time.sleep(5)
            mut_ingreso.release()
            max_ingreso.wait()
            
        else:
            #nuevoIngt.acquire()
            #telefonos.append(1)
            nuevoIngt.release()
        llamadasEntrante.release()
        print("Esperando llamada")
        time.sleep(5)
        llamadasEntrante.release()
        #print("Sonando el telefono, Rinrinrin")
        #llamadasEntrante.acquire
        #mut_ingreso.acquire()
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
mut_egreso=Semaphore(0)
mut_ingreso=Semaphore(1)
max_ingreso=Barrier(9,saturacion)
servicios=["Policias","Bomberos","Ambulancia"]
numllamadas=[]
llamadas=[]
telefonos=[]
Thread(target=main,args=[]).start()
'''Formar una lista de telefonos para ver si hay disponibilidad
con 10 telefonos, remplazando con 1 para ver disponibilidad de telefonos con 
base a la funcion de ingreso'''
