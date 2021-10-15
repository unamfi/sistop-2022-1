#           Universidad Nacional Autonoma de Mexico
#                   Facultad de Ingenieria
#                       Sistemas Operativos
#
#           Desarrollador:
#               Hernandez Campuzano Ivan
#           Profesor:
#               Gunnar Wolf
#           Descripcion:
#               Este programa solo simula la ateancion de una duda por 
#               cierta cantidad de alumnos y si no hay alumnos que 
#               asesorar duerme el asesor
#
from threading import Semaphore, Thread
import time
import random

cuenta = 0
num_alumnos = 9
descansa_asesor = Semaphore(0)
mutex = Semaphore(1)
torniquete = Semaphore(1)
duda = Semaphore(2)
cubiculo = Semaphore (0)
def asesor():
    global duda
    while(True):
        global cuenta, num_alumnos,mutex, duda
        duda.acquire()
        print("Asesor dando asesoria")
        time.sleep(3)
        duda.release() 
        #print(cuenta)
        if cuenta == num_alumnos:
            print("Asesor se va a dormir")
            descansa.asesor.acquire()

def alumnos(id):
    global cuenta, mutex, duda
    
    torniquete.acquire()
    time.sleep(1)
    torniquete.release()
    mutex.acquire()
    cuenta = cuenta + 1
    duda.acquire()
    print("Alumno %d tomando asesoria" % id)
    time.sleep(3)
    duda.release()
    mutex.release()
    
  
            

Thread(target=asesor).start()
for i in range(num_alumnos):
    Thread(target=alumnos, args=[i]).start()

