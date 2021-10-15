#!/usr/bin/python3
# @author: Eduardo Peralta
# 
# Reglas:
# - En la balsa caben cuatro (y sólo cuatro) personas
# - La balsa es demasiado ligera, y con menos de cuatro puede volcar.

# - Al encuentro están invitados hackers (desarrolladores de Linux) y serfs (desarrolladores de Microsoft).
# - Para evitar peleas, debe mantenerse un buen balance: No debes permitir que aborden tres hackers y un serf, o tres serfs y
#  un hacker. Pueden subir cuatro del mismo bando, o dos y dos.

import threading
import time
import random
import sys

#Variables:

personas = 0    #integrantes en el bote
num_hack = 0    #numero de hackers
num_serf = 0    #numero de serfs

hackers_ = threading.Semaphore(0)
serfs_ = threading.Semaphore(0)

mutex = threading.Semaphore(1)
mutex_boat = threading.Semaphore(1)

def hackers():
    global num_hack
    global num_serf
    global mutex
    mutex.acquire()
    num_hack += 1

    if num_hack == 4:
        hackers_.release()
        hackers_.release()
        hackers_.release()
        num_hack = 0
        mutex.release()
        acomodar("pinguino"," 🐧 ")
    elif (num_hack == 2 and num_serf == 2):
        hackers_.release()
        serfs_.release()
        serfs_.release()
        num_hack = 0
        num_serf = 0
        mutex.release()
        acomodar("pinguino"," 🐧")
    else:
        mutex.release()
        hackers_.acquire()
        acomodar("pinguino"," 🐧")


def serfs():
    global num_hack
    global num_serf
    global mutex
    mutex.acquire()
    num_serf += 1

    if num_serf == 4:
        serfs_.release()
        serfs_.release()
        serfs_.release()
        num_serf = 0
        mutex.release()
        acomodar("ventana"," 🗔")
    elif(num_hack == 2 and num_serf == 2):
        hackers_.release()
        hackers_.release()
        serfs_.release()
        num_hack = 0
        num_serf = 0
        mutex.release()
        acomodar("ventana"," 🗔")
    else:
        mutex.release()
        serfs_.acquire()
        acomodar("ventana"," 🗔")




def acomodar(desarrollador,icon):
    global personas
    mutex_boat.acquire()
    personas += 1
    print("║ Subiendo un@ "+desarrollador+" ║"+icon)
    if personas == 4:
        print("==== Momento de irnos ====")
        personas = 0
    mutex_boat.release()



print("En un convencion en donde hay desarrolladores de"+ 
    "sistemas operativos, encontramos pinguinos (desarrolladores " +
    "de Linux) y ventanas (desarrolladores de Windows) observemos como"+
    " llegan a cruzar un rio para llegar a su destino")
try:
    while True:
        if round(random.choice([0,1])) == 0:
            threading.Thread(target = hackers, args = []).start()
            time.sleep(0.5)
        else:
            threading.Thread(target = serfs, args = []).start()
            time.sleep(0.5)


except KeyboardInterrupt:
    print("║║ Ya terminamos de pasar a todos ║║")
    sys.exit()


