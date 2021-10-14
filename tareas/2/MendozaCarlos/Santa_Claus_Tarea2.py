# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:12:19 2021

@author: Carlo
"""

from threading import Barrier,Thread,Semaphore
import random
import time

def renos(num,tiempovaca):
    while True:
       renos_mutex.acquire()
       print("Reno ",num ," esta de vacaciones\n") 
       renos_mutex.release()
       time.sleep(tiempovaca)
       renos_mutex.acquire()
       print("El reno" ,num ," ya llego\n ")
       renos_mutex.release()
       time.sleep(tiempovaca)
       barrier.wait()
       if (num==9):
           renos_mutex.acquire()
           print("Despertar a santa, a trabajar")
           renos_mutex.release()
       
    
def elfos(num):
    global mut_elfos
    while True:
        mut_elfos.acquire()
        problema_elfo=random.randint(0, 10)
        mut_elfos.release()
        if problema_elfo==10:
            time.sleep(5)
            mut_elfos.acquire()
            print("Tengo problema, soy el elfo ",num, "\n ")
            elfos_problemas.append(num) #Agregamos los elfos
            mut_elfos.release()
            barrera_elfos.wait()#Si son 3 elfos se va a elfos_ayuda
            
    
    
def elfos_ayuda():
        print("AYUDA SANTA POR FAVOR " , elfos_problemas)
        elfos_problemas.clear()
        print("Muchas gracias Santa, dicen los elfos",)
def santa():
    global santa_estado
    santa_estado.acquire()
    #elfos_situacion.acquire()
    print("Santa dormido")
    
    
    #santa_estado.release()
renos_mutex=Semaphore(1)
santa_estado=Semaphore(1)
mut_elfos=Semaphore(1)
barrier=Barrier(9)
barrera_elfos=Barrier(3,elfos_ayuda) 
num_elfos=random.randint(5,100)
num_renos=9
elfos_problemas=[]
santa()
for renos_id in range(1,num_renos+1):
    reno_num=Thread(target=renos,args=[renos_id,3]).start()
for elfos_id in range(1,num_elfos+1):
    elfos_num=Thread(target=elfos,args=[elfos_id]).start()