from threading import Semaphore
from threading import Thread
import random
import time
import sys

#Recursos compartidos del programa
elfo_counter = 0 
reno_counter = 0 

#Semaforos que administran el acceso a los recursos compartidos entre todos los hilos
mutex = Semaphore(1) 
elfTex = Semaphore() 
reno_sem = Semaphore() 
santa_sem = Semaphore() 

#Mensajes predefinidos de acción 
def renos_listos(): 
    print("Los 9 renos han llegado, Santa se prepara para salir")

def ayuda_elfos():
    print("╬"+"═"*25+"╬")
    print("║ Santa ayuda a sus elfos ║")
    print("╬"+"═"*25+"╬")

def llegada_reno():
    print("--> Llego el reno ", reno_counter)

def ayuda_elfo():
    print( elfo_counter,"elfo(s) pidio/pidieron ayuda")

def santa_wake_up():
    print("╔"+"═"*53+"╗")    
    print("║ Santa se desperto, a repartir regalos a los mocosos ║")
    print("║ Santa regresó al polo.Los renos estan de vacaciones ║")
    print("╚"+"═"*53+"╝") 

def santa_to_sleep():
    print("┼"+"─"*27+"┼")
    print("│ Santa Claus se va a mimir │")
    print("┼"+"─"*27+"┼")

#El proceso Santa verifica el valor de los recursos compartidos, una vez verificado decide si se despierta o sigue mimiendo
def santa():
    global elfo_counter, reno_counter
    santa_to_sleep()
    while True:
        santa_sem.acquire()
        mutex.acquire()
        if reno_counter >= 9:
            renos_listos()
            for i in range(9):
                reno_sem.release()
            santa_wake_up() 
            reno_counter -= 9
            time.sleep(3)
        elif elfo_counter == 3:
            ayuda_elfos()
        mutex.release()

#El proceso de los renos modifican el recurso compartido contador de renos, y puede a despertar a Santa
def reno():
    global reno_counter
    while True:
        mutex.acquire()
        reno_counter += 1
        if reno_counter == 9:
            santa_sem.release()
        mutex.release()
        llegada_reno()
        reno_sem.acquire()
        time.sleep(random.randint(2, 3))

#El proceso de los elfos modifican el recurso compartido contador de elfos, y puede a despertar a Santa
def elfo():
    global elfo_counter
    while True:
        elfTex.acquire()
        mutex.acquire()
        elfo_counter += 1
        if elfo_counter == 3:
            santa_sem.release()
        else:
            elfTex.release()
        mutex.release()
        ayuda_elfo()
        time.sleep(random.randint(2, 5))
        mutex.acquire()
        elfo_counter -= 1
        if elfo_counter == 0:
            elfTex.release()
        mutex.release()
        #print(elfo_counter, "regresa al trabajo")

# Almacenamos los hilos de los elfos y renos
hilos_elfos = []  
hilos_reno = []  


def main():
    num_elf = int(input("¿Cuántos elfos hay en el polo norte?\n-->"))

    main_thread = Thread(target=santa)  # Creamos e iniciamos el hilo de Santa 
    main_thread.start() 

    for i in range(9):
        hilos_reno.append(Thread(target=reno)) #Creamos los hilos de los renos
    for j in range(num_elf):
        hilos_elfos.append(Thread(target=elfo))  #Creamos los hilos de los elfos
    #Iniciamos los hilos 
    for h in hilos_elfos:
        h.start()           
    for h in hilos_reno:
        h.start()
    for h in hilos_elfos:
        h.join()
    for h in hilos_reno:
        h.join()
    main_thread.join()


main()