from threading import Semaphore,Thread
import random
import time

def entrada(id_entrada):
    print('Soy la puerta %d' %id_entrada)

def visitantes(id_visitante):
    mutex_visitante.acquire()
    print('Soy el visitante %d y quiero entrar' %id_visitante)
    temperatura = random.randint(35,40)
    print('Soy el visitante %d y mi temperatura es de %d' %(id_visitante,temperatura))
    puerta_a_usar = random.randint(1,4)
    print('Soy el visitante %d y quiero entrar por la puerta %d' %(id_visitante,puerta_a_usar))
    if puerta_a_usar == 1:
        entrada_1.append(id_visitante)
        print(entrada_1)
    elif puerta_a_usar == 2:
        entrada_2.append(id_visitante)
        print(entrada_2)
    elif puerta_a_usar == 3:
        entrada_3.append(id_visitante)
        print(entrada_3)
    elif puerta_a_usar == 4:
        entrada_4.append(id_visitante)
        print(entrada_4)
    mutex_visitante.release()

#Iniciamos las colas en las que se van a formar los visitantes para cada entrada
entrada_1 = []
entrada_2 = []
entrada_3 = []
entrada_4 = []
mutex_visitante = Semaphore(1)
#cantidad total de vistantes del centro comercial
num_visitantes = 10
#cantidad total de entradas del centro comercial
num_entradas = 4
for id_visitante in range(num_visitantes):
    Thread(target=visitantes, args=[id_visitante]).start()
for id_entrada in range(num_entradas):
    Thread(target=entrada, args=[id_entrada]).start()
