# -*- coding: utf-8 -*-
#Inspirado en el codigo que realizó el profesor Gunnar Wolf para este ejercicio
import threading as th
import time
import random as rdm
     
def reno(identificador):
    #Si vuelven los nueve renos entonces Santa Claus despierta
    while True:
        print("  El Reno_%d: está de vacaciones" % identificador)
        #simulacion de las vaciones
        time.sleep(rdm.random()*4)
        print("  El Reno_%d: está en camino a casa" % identificador)
        barrera_r.wait()
        #Despierta santa cuando llega el lider de los renos 
        #Rodolfo = Reno_0
        if identificador==0:
            print( "Hora de trabajar Santa!")
            #Hay que despertar a santa
            d_santa.release()
        
        #Ya no se requieren a los renos
        vacaciones[identificador].acquire()
        
def mamá_Claus(elfos_espera):
    d_mamá.release()
    print('Hora de trabajar por Santa ')
    while len(elfos_con_problemas) > 3:
        identificador_elfo= elfos_con_problemas.pop()
        print('Mamá ayudándole al elfo %d' % identificador_elfo )
    mutex_elfos.release()

      
def santa():
    while True:
        d_santa.acquire()
        mutex_elfos.acquire()
        elfos_espera = len(elfos_con_problemas)
        mutex_elfos.release()
        if elfos_espera >= 3:
            # Deberían ser sólo tres elfos pero ellos no descansan ningun dia.
            mutex_elfos.acquire()
            while len(elfos_con_problemas) > 0:
                identificador_elfo= elfos_con_problemas.pop()
                print('Santa ayudándole al elfo %d' % identificador_elfo)
            mutex_elfos.release()
        else:
            print("Hora de comer galletas")
            #Se fué santa, le toca a mamá Claus ayudar
            #mamá_Claus(elfos_espera)
            #tiempo trabajando(...)
            time.sleep(3)
        #finalizando trabajo(...)
        #renos pueden descansar(...)
        for i in range(cant_renos):
            vacaciones[i].release()

def elfo(identificador):
    while True:
        time.sleep(rdm.random())
        denle_elfos.acquire()
        denle_elfos.release()
        if rdm.random() < 0.01:           
            print('      Elfo_%d: problema :-(' % identificador)
            soy_el_primero = False
            # Tuve un problema construyendo mi juguete :-(
            mutex_elfos.acquire()
            elfos_con_problemas.append(identificador)
            elfos_espera=len(elfos_con_problemas)
            if elfos_espera>=4:
                mamá_Claus(elfos_espera)
            else:
                print('      Elfo_%d: Hay %d elfos esperando' % (identificador, len(elfos_con_problemas)))
                if len(elfos_con_problemas) == 1:
                    soy_el_primero = True
                mutex_elfos.release()
                barrera_e.wait()
                if soy_el_primero:
                   print('      Elfo_%d: despierta a Santa' % identificador)
                   d_santa.release()



molestos=3                                                 #Santa solo tolera a 3 elfos        
cant_elfos=100                                             #Santa tiene n elfos
cant_renos=9                                               #Santa tiene 9 renos
elfos_con_problemas=[]                                     #Sólo pueden haber 3
barrera_r=th.Barrier(cant_renos)                           #Sólo deben llegar 9 renos para que Santa Claus despierte
barrera_e=th.Barrier(molestos)                             #Sólo pueden ir de 3 en 3 elfos con Santa

d_santa=th.Semaphore(0)                                    #Santa está dormido
d_mamá=th.Semaphore(0)                                     #Mamá Claus está dormida
vacaciones=[th.Semaphore(0)for i in range(cant_renos)]     #Nueve semaforos

mutex_elfos=th.Semaphore(1)                                #Mutex para elfos
denle_elfos=th.Semaphore(1)

th.Thread(target=santa).start()
th.Thread(target=mamá_Claus).start()
#Crear 9 renos
for identificador_reno in range(cant_renos):
    th.Thread(target=reno, args=[identificador_reno]).start()
#Crear n elfos
for identificador_elfo in range(cant_elfos):
    th.Thread(target=elfo, args=[identificador_elfo]).start()

