from threading import Barrier,Thread,Semaphore
import random
import time


def ingresos(num):
    global llamadas,mut_ingreso,max_telefonos
    while True:
        numllamadas.append(1)
        mut_ingreso.acquire()
        print("Atendiendo una llamada",num)
        time.sleep(4)
        mut_ingreso.release()
        print("Lista ",numllamadas, "longitud ", len(numllamadas))
        #max_ingreso.wait()
        if len(numllamadas)<=max_telefonos:
           # mut_ingreso.acquire()
            
           # print("Llamadas en espera",llamadas)
            llamadas.append(num)
            numllamadas.clear
            #mut_ingreso.release()
            max_ingreso.wait()

            #max_ingreso.wait()
        #Thread(target=egreso,args=[]).start()
def saturacion():
    print("Llamadas en espera ", llamadas)
    llamadas.clear
def egreso():
    global nuevoEgr,servicios,ayuda
    while True:
        #nuevoEgr.acquire()
        nuevoEgr.acquire
        print("Esperando una llamada")
        time.sleep(5)
        nuevoEgr.release()
        #print("Atendiendo la llamada ",llamadas)
        if ayuda<random.randint(1,100):
             nuevoEgr.acquire()
             print("Llamando a ",random.choice(servicios))
             time.sleep(5)
             nuevoEgr.release()


def main():
    parametros=random.randint(10, 15)
    for num_llamadas in range(1,parametros):
        Thread(target=ingresos,args=[num_llamadas]).start()
    for num_Egreso in range(1,parametros):
        Thread(target=egreso,args=[]).start()
    #for num_llamadasE in range(1,random.randint(2,15)):
    #Thread(target=egreso,args=[]).start()

ayuda=50
max_telefonos=10
nuevoIngt=Semaphore(1)
nuevoEgr=Semaphore(0)
mut_egreso=Semaphore(1)
mut_ingreso=Semaphore(1)
max_ingreso=Barrier(10,saturacion)
servicios=["Policias","Bomberos","Ambulancia"]
numllamadas=[]
llamadas=[]
main()
