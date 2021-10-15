#Fuerte Martínez Nestor Enrique
#Tafolla Rosales Esteban

import threading
import time
import random

gatos_numero = 2
ratones_numero = 4

plato_disp = threading.Semaphore(0) #hay platos disponibles 
gato_existe = threading.Semaphore(0) #hay gatos que no hayan terminado de comer

gatos_res = 0

mut_acceso = threading.Semaphore(1)
mut_platos = threading.Semaphore(2)
gatos = threading.Semaphore(1)
ratones = threading.Semaphore(1)
mut_protege_bandera = threading.Semaphore(1)

gatos_en_plato = 0
raton_en_plato = 0
num_plato = 0
bandera = 1

def gato():
    global mut_platos, mut_gato, gatos, gatos_en_plato, raton_en_plato, mut_protege_bandera, bandera, ratones, ratones_numero    
    print("Soy un gato")
    while ( ratones_numero > 1 ):
        time.sleep( random.random() )
        if(raton_en_plato==0):
            gatos.acquire()
            gatos_en_plato += 1
            gatos.release()
            mut_platos.acquire() #Bloquea para que nadie acceda en lo que lo usa 
            print("Soy un gato y como en el plato ")
            time.sleep( random.random() )
            mut_platos.release() #Devuelve para que los demas lo usen  
            gatos.acquire()
            gatos_en_plato -= 1
            gatos.release()
            print("El gato termino de comer")
        else:
            if(raton_en_plato==2):
                print("Por honor dejare comer a los ratones")

            else:
                gatos.acquire()
                gatos_en_plato += 1
                gatos.release()
                print("Comamos al raton")            
                time.sleep( random.random() )
                print("El gato termino de comer al raton %d" %ratones_numero)
                
                gatos.acquire()
                gatos_en_plato -= 1
                gatos.release()
                ratones.acquire()
                raton_en_plato -=1
                ratones.release()
                ratones.acquire()
                ratones_numero-=1
                ratones.release()
                mut_protege_bandera.acquire()
                bandera = 0
                mut_protege_bandera.release()
                      
def raton():
    global mut_platos, gatos_en_plato, raton_en_plato, mut_protege_bandera, bandera, ratones
    print("Soy un raton")
    while (ratones_numero > 1):
        time.sleep( random.random() )
        if(gatos_en_plato==0):
            mut_platos.acquire() #Bloquea para que nadie acceda en lo que lo usa 
            ratones.acquire()
            raton_en_plato += 1
            ratones.release()
            print("No hay gatos a la vista, a comer")
            time.sleep( random.random() )
            mut_protege_bandera.acquire()
            if(bandera):
                mut_platos.release() #Devuelve para que los demas lo usen  
                print("Ya Acabe de comer gracias, dijo el raton")
                mut_protege_bandera.release()
            else:
                mut_platos.release() #Devuelve para que los demas lo usen  
                bandera = 1
                mut_protege_bandera.release()
            ratones.acquire()
            raton_en_plato -= 1
            ratones.release()
        else:
            
            print("No comi porque el gato no me dejo")
    
def iniciar():

    for i in range(gatos_numero):
        threading.Thread(target=gato, args=[]).start()
    for i in range(ratones_numero):
        threading.Thread(target=raton, args=[]).start()
    
iniciar()