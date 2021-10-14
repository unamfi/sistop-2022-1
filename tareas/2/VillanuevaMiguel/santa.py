import threading
import random
import time

def elfo(idelfos):
    while True:
        
        if (random.random() < 0.1):
            time.sleep(3)
            muElfos.acquire()
            print("Soy el elfo" ,idelfos, "y tengo un problema aqui")
            muElfos.release()
            barreraElfos.wait()
            elfoProblemas.acquire()
        
def reno(idrenos):
    while True:
        time.sleep(random.random()*3)
        muRenos.acquire()
        print (" se fue el reno ",idrenos)
        muRenos.release()
        time.sleep(random.random()*5)
        muRenos.acquire()
        print("A regresado el reno ",idrenos)
        muRenos.release()
        
        barreraRenos.wait()
        if idrenos==8:
            muRenos.acquire()
            print("\n Estamos todos, listos para el viaje!")
            muRenos.release()
        vacaciones.acquire()
        
def santa():
    while True:
       muRenos.acquire()
       vacaciones.release()
       muRenos.release()

       muElfos.acquire()
       elfoProblemas.release()
       muElfos.release()
      
def ayuda():
       muElfos.acquire()
       print("Santa te ayudara!")
       muElfos.release()
            
    
renos=9
elfos=100
vacaciones=threading.Semaphore(0)
NocheBuena= threading.Semaphore(0)
muRenos=threading.Semaphore(1)
barreraRenos=threading.Barrier(9)

elfoProblemas=threading.Semaphore(0)
muElfos=threading.Semaphore(1)
barreraElfos=threading.Barrier(3,ayuda)

threading.Thread(target=santa).start()
for idrenos in range(renos):
    threading.Thread(target=reno, args=[idrenos]).start()
for idelfos in range(elfos):
    threading.Thread(target=elfo, args=[idelfos]).start()