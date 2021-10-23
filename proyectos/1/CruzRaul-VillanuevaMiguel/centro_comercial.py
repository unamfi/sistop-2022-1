from threading import Semaphore,Thread,Barrier
import random
import time

def visitantes(id_visitante):
    mutex_visitante.acquire()
    temperatura = random.randint(35,40)
    puerta_a_usar = random.randint(1,4)
    time.sleep(2)
    print('Soy el visitante %d y quiero entrar' %id_visitante)
    print("mi temperatura es de %d y quiero entrar por la puerta %d" %(temperatura,puerta_a_usar))
    #print('mi temperatura es de %d' %temperatura)
    #print('y quiero entrar por la puerta %d' %puerta_a_usar)
    if puerta_a_usar == 1:
        entrada_1.append(id_visitante)
        print(entrada_1)
        if temperatura > 37:
            print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
            entrada_1.remove(id_visitante)
            print(entrada_1)
        else:
            print("Pase Usted")
            plaza.append(id_visitante)
            #barrera1.wait()
            compras(id_visitante)
    elif puerta_a_usar == 2:
        entrada_2.append(id_visitante)
        print(entrada_2)
        if temperatura > 37:
            print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
            entrada_2.remove(id_visitante)
            print(entrada_2)
        else:
            print("Pase Usted")
            plaza.append(id_visitante)
            #barrera1.wait()
            compras(id_visitante)
    elif puerta_a_usar == 3:
        entrada_3.append(id_visitante)
        print(entrada_3)
        if temperatura > 37:
            print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
            entrada_3.remove(id_visitante)
            print(entrada_3)
        else:
            print("Pase Usted")
            plaza.append(id_visitante)
            #barrera1.wait()
            compras(id_visitante)
    elif puerta_a_usar == 4:
        entrada_4.append(id_visitante)
        print(entrada_4)
        if temperatura > 37:
            print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
            entrada_4.remove(id_visitante)
            print(entrada_4)
        else:
            print("Pase Usted")
            plaza.append(id_visitante)
            #barrera1.wait()
            compras(id_visitante)
    print(plaza)
    mutex_visitante.release()
    
def salida():
    print("De regreso a casita")

def compras(id_visitante):
    print("yupi %d va de compras" %id_visitante)

#Iniciamos las colas en las que se van a formar los visitantes para cada entrada
entrada_1 = []
entrada_2 = []
entrada_3 = []
entrada_4 = []
plaza=[]
mutex_visitante = Semaphore(1)
id_visitante=0
#barrera1=Barrier(1,compras)
#cantidad total de vistantes del centro comercial
num_visitantes = 10
#cantidad total de entradas del centro comercial
num_entradas = 4
for id_visitante in range(num_visitantes):
    Thread(target=visitantes, args=[id_visitante]).start()
#for id_entrada in range(num_entradas):
#    Thread(target=entrada, args=[id_entrada]).start()