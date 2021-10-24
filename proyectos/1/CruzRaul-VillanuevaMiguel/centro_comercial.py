from threading import Semaphore,Thread,Barrier
import random
import time

def visitantes(id_visitante):
    mutex_visitante.acquire()
    
    temperatura = random.randint(35,40)
    puerta_a_usar = random.randint(1,4)
    #time.sleep(2)
    print('Soy el visitante %d y quiero entrar' %id_visitante)
    print("mi temperatura es de %d y quiero entrar por la puerta %d" %(temperatura,puerta_a_usar))
    if puerta_a_usar == 1:
        entrada_1.append([id_visitante,temperatura])
        print(entrada_1)
    elif puerta_a_usar == 2:
        entrada_2.append([id_visitante,temperatura])
        print('Desde visitantes ',entrada_2)
    elif puerta_a_usar == 3:
        entrada_3.append([id_visitante,temperatura])
        print('Desde visitantes ',entrada_3)
    elif puerta_a_usar == 4:
        entrada_4.append([id_visitante,temperatura])
        print('Desde visitantes ',entrada_4)
    print('Desde visitantes plaza',plaza)
    mutex_visitante.release()
    #mutex_entrada.release()
    
def entradas(id_entrada):
    time.sleep(5)
    mutex_entrada.acquire()
    if id_entrada == 1:
        entrada_1_eliminados = []
        contador_para_eliminar_1=0
        longitud = len(entrada_1)
        for i in range(longitud):
            temperatura = entrada_1[i][1]
            id_visitante = entrada_1[i][0]
            if temperatura > 37:
                print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
                entrada_1_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_1 = contador_para_eliminar_1+1
            else:
                print("Pase Usted")
        for i in range(contador_para_eliminar_1):
            id_visitante = entrada_1_eliminados[i][0]
            temperatura = entrada_1_eliminados[i][1]
            entrada_1.remove([id_visitante,temperatura])
        print('Lista definitiva 1: ',entrada_1)
        
    if id_entrada == 2:
        entrada_2_eliminados = []
        contador_para_eliminar_2=0
        longitud = len(entrada_2)
        for i in range(longitud):
            temperatura = entrada_2[i][1]
            id_visitante = entrada_2[i][0]
            if temperatura > 37:
                print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
                entrada_2_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_2 = contador_para_eliminar_2+1
            else:
                print("Pase Usted")
        for i in range(contador_para_eliminar_2):
            id_visitante = entrada_2_eliminados[i][0]
            temperatura = entrada_2_eliminados[i][1]
            entrada_2.remove([id_visitante,temperatura])
        print('Lista definitiva 2: ',entrada_2)
    
    if id_entrada == 3:
        entrada_3_eliminados = []
        contador_para_eliminar_3=0
        longitud = len(entrada_3)
        for i in range(longitud):
            temperatura = entrada_3[i][1]
            id_visitante = entrada_3[i][0]
            if temperatura > 37:
                print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
                entrada_3_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_3 = contador_para_eliminar_3+1
            else:
                print("Pase Usted")
        for i in range(contador_para_eliminar_3):
            id_visitante = entrada_3_eliminados[i][0]
            temperatura = entrada_3_eliminados[i][1]
            entrada_3.remove([id_visitante,temperatura])
        print('Lista definitiva 3: ',entrada_3)
    
    if id_entrada == 4:
        entrada_4_eliminados = []
        contador_para_eliminar_4=0
        longitud = len(entrada_4)
        for i in range(longitud):
            temperatura = entrada_4[i][1]
            id_visitante = entrada_4[i][0]
            if temperatura > 37:
                print("No puede acceder su temperatura es de %d ,visite a su doctor para un diagnostico" %temperatura)
                entrada_4_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_4 = contador_para_eliminar_4+1
            else:
                print("Pase Usted")
        for i in range(contador_para_eliminar_4):
            id_visitante = entrada_4_eliminados[i][0]
            temperatura = entrada_4_eliminados[i][1]
            entrada_4.remove([id_visitante,temperatura])
        print('Lista definitiva 4: ',entrada_4)
    mutex_entrada.release()

def compras(id_visitante):
    mutex_entrada.acquire()
    print("¡Yupi! %d va de compras" %id_visitante)
    #El visitante elige a cuál tienda ir
    comprar_en = random.randint(1,6)
    #si comprar_en es igual a 1, se va a Suburbia
    if comprar_en == 1:
        print('¡Iré a Suburbia! Seguro encuentro algo bonito para ponerme :D %d' %id_visitante)
        #time.sleep(3)
    #si comprar_en es igual a 2, se va a ZorzalMusic (tienda de discos y audífonos)
    if comprar_en == 2:
        print('Tengo ganas de buena música, ¡iré a ZorzalMusic! %d' %id_visitante)
        #time.sleep(2)
    #si comprar_en es igual a 3, se va a Petco
    if comprar_en == 3:
        print('Si voy a Petco, seguro habrá algo binito para mi mascota <3 %d' %id_visitante)
        #time.sleep(3)  
    #si comprar_en es igual a 4, se va a Cex (tienda de videojuegos)
    if comprar_en == 4:
        print('¿La gente sigue comprando videojuegos en fisico? Tal vez lo haga después de mucho tiempo %d' %id_visitante)
        #time.sleep(2)
    #si comprar_en es igual a 5, se va a The Cheesecake Factory
    if comprar_en == 5:
        print('Tengo ganas de romper la dieta, ¡iré a The Cheesecake Factory! %d' %id_visitante)
        #time.sleep(4)
    #si comprar_en es igual a 6, se va a Cinemex
    if comprar_en == 6:
        print('Ya extrañaba ir al cina, ¡es hora de ir a Cinemex! %d' %id_visitante)
        #time.sleep(6)
    mutex_entrada.release()
    
def salida():
    print("De regreso a casita")
    
#Iniciamos las colas en las que se van a formar los visitantes para cada entrada
entrada_1 = []
entrada_2 = []
entrada_3 = []
entrada_4 = []
plaza=[]
mutex_visitante = Semaphore(1)
mutex_entrada = Semaphore(1)
id_visitante=0

#cantidad total de vistantes del centro comercial
num_visitantes = 10
#cantidad total de entradas del centro comercial
num_entradas = 4
#invocamos a los hilos
for id_visitante in range(num_visitantes):
    Thread(target=visitantes, args=[id_visitante]).start()
for id_entrada in range(1,num_entradas+1):
    Thread(target=entradas, args=[id_entrada]).start()