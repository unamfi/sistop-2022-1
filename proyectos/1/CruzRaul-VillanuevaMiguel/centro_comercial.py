from threading import Semaphore,Thread
import random
import time

def visitantes(id_visitante):
    mutex_visitante.acquire()
    temperatura = random.randint(35,39)
    puerta_a_usar = random.randint(1,4)
    time.sleep(0.2)
    print('Soy el visitante %d y quiero entrar' %id_visitante)
    print("mi temperatura es de %d y quiero entrar por la puerta %d" %(temperatura,puerta_a_usar))
    #Lo formamos en la cola de la puerta en la que entrará
    if puerta_a_usar == 1:
        entrada_1.append([id_visitante,temperatura])
        print('Nosotros estamos formado en la fila: ',entrada_1)
    elif puerta_a_usar == 2:
        entrada_2.append([id_visitante,temperatura])
        print('Nosotros estamos formado en la fila: ',entrada_2)
    elif puerta_a_usar == 3:
        entrada_3.append([id_visitante,temperatura])
        print('Nosotros estamos formado en la fila: ',entrada_3)
    elif puerta_a_usar == 4:
        entrada_4.append([id_visitante,temperatura])
        print('Nosotros estamos formado en la fila: ',entrada_4)
    print('\n')
    mutex_visitante.release()
    
def entradas(id_entrada):
    global personas_dentro
    time.sleep(5)
    #Le damos al hilo la cola que le corresponde atender
    if id_entrada == 1:
        entrada_1_eliminados = []
        contador_para_eliminar_1=0
        longitud = len(entrada_1)
        for i in range(longitud):
            temperatura = entrada_1[i][1]
            id_visitante = entrada_1[i][0]
            #No dejamos que ingresen aquello con temperatura alta
            if temperatura > 37:
                print("Visitante %d, no puede acceder su temperatura es de %d, visite a su doctor para un diagnóstico\n" %(id_visitante,temperatura))
                entrada_1_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_1 = contador_para_eliminar_1+1
            else:
                mutex_impresion.acquire()
                print('Visitante %d, pase Usted' % id_visitante)
                visitantes_maximos.acquire()
                plaza.append(id_visitante)
                personas_dentro = len(plaza)
                print('Entró una persona, hay: %d'% personas_dentro)
                compras(id_visitante)
        #Eliminamos de la cola a los visitantes con acceso restringido
        for i in range(contador_para_eliminar_1):
            id_visitante = entrada_1_eliminados[i][0]
            temperatura = entrada_1_eliminados[i][1]
            entrada_1.remove([id_visitante,temperatura])
        
    if id_entrada == 2:
        entrada_2_eliminados = []
        contador_para_eliminar_2=0
        longitud = len(entrada_2)
        for i in range(longitud):
            temperatura = entrada_2[i][1]
            id_visitante = entrada_2[i][0]
            if temperatura > 37:
                print("Visitante %d, no puede acceder su temperatura es de %d, visite a su doctor para un diagnóstico\n" %(id_visitante,temperatura))
                entrada_2_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_2 = contador_para_eliminar_2+1
            else:
                mutex_impresion.acquire()
                print('Visitante %d, pase Usted' % id_visitante)
                visitantes_maximos.acquire()
                plaza.append(id_visitante)
                personas_dentro = len(plaza)
                print('Entró una persona, hay: %d'% personas_dentro)
                compras(id_visitante)
        for i in range(contador_para_eliminar_2):
            id_visitante = entrada_2_eliminados[i][0]
            temperatura = entrada_2_eliminados[i][1]
            entrada_2.remove([id_visitante,temperatura])
    
    if id_entrada == 3:
        entrada_3_eliminados = []
        contador_para_eliminar_3=0
        longitud = len(entrada_3)
        for i in range(longitud):
            temperatura = entrada_3[i][1]
            id_visitante = entrada_3[i][0]
            if temperatura > 37:
                print("Visitante %d, no puede acceder su temperatura es de %d, visite a su doctor para un diagnóstico\n" %(id_visitante,temperatura))
                entrada_3_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_3 = contador_para_eliminar_3+1
            else:
                mutex_impresion.acquire()
                print('Visitante %d, pase Usted' % id_visitante)
                visitantes_maximos.acquire()
                plaza.append(id_visitante)
                personas_dentro = len(plaza)
                print('Entró una persona, hay: %d'% personas_dentro)
                compras(id_visitante)
        for i in range(contador_para_eliminar_3):
            id_visitante = entrada_3_eliminados[i][0]
            temperatura = entrada_3_eliminados[i][1]
            entrada_3.remove([id_visitante,temperatura])
    
    if id_entrada == 4:
        entrada_4_eliminados = []
        contador_para_eliminar_4=0
        longitud = len(entrada_4)
        for i in range(longitud):
            temperatura = entrada_4[i][1]
            id_visitante = entrada_4[i][0]
            if temperatura > 37:
                print("Visitante %d, no puede acceder su temperatura es de %d, visite a su doctor para un diagnóstico\n" %(id_visitante,temperatura))
                entrada_4_eliminados.append([id_visitante,temperatura])
                contador_para_eliminar_4 = contador_para_eliminar_4+1
            else:
                mutex_impresion.acquire()
                print('Visitante %d, pase Usted' % id_visitante)
                visitantes_maximos.acquire()
                plaza.append(id_visitante)
                personas_dentro = len(plaza)
                print('Entró una persona, hay: %d'% personas_dentro)
                compras(id_visitante)
        for i in range(contador_para_eliminar_4):
            id_visitante = entrada_4_eliminados[i][0]
            temperatura = entrada_4_eliminados[i][1]
            entrada_4.remove([id_visitante,temperatura])

def compras(id_visitante):
    global personas_dentro
    print("¡Yupi! por fin voy de compras (:")
    #El visitante elige a cuál tienda ir
    comprar_en = random.randint(1,6)
    #si comprar_en es igual a 1, se va a Suburbia
    if comprar_en == 1:
        print('¡Iré a Suburbia! Seguro encuentro algo bonito para ponerme :D\n')
        mutex_impresion.release()
        time.sleep(random.randint(5,11))
        mutex_salida.acquire()
        print('El visitante %d se va. ¡Vuleva pronto!\n' %id_visitante)
        mutex_salida.release()
        plaza.remove(id_visitante)
        personas_dentro = len(plaza)
        visitantes_maximos.release()
    #si comprar_en es igual a 2, se va a ZorzalMusic (tienda de discos y audífonos)
    if comprar_en == 2:
        print('Tengo ganas de buena música, ¡iré a ZorzalMusic!\n')
        mutex_impresion.release()
        time.sleep(random.randint(5,11))
        mutex_salida.acquire()
        print('El visitante %d se va. ¡Vuleva pronto!\n' %id_visitante)
        mutex_salida.release()
        plaza.remove(id_visitante)
        personas_dentro = len(plaza)
        visitantes_maximos.release()
    #si comprar_en es igual a 3, se va a Petco
    if comprar_en == 3:
        print('Si voy a Petco, seguro habrá algo bonito para mi mascota <3\n')
        mutex_impresion.release()
        time.sleep(random.randint(5,11))
        mutex_salida.acquire()
        print('El visitante %d se va. ¡Vuleva pronto!\n' %id_visitante)
        mutex_salida.release()
        plaza.remove(id_visitante)
        personas_dentro = len(plaza)
        visitantes_maximos.release()
    #si comprar_en es igual a 4, se va a Cex (tienda de videojuegos)
    if comprar_en == 4:
        print('¿La gente sigue comprando videojuegos en fisico? Tal vez lo haga después de mucho tiempo\n')
        mutex_impresion.release()
        time.sleep(random.randint(5,11))
        mutex_salida.acquire()
        print('El visitante %d se va. ¡Vuleva pronto!\n' %id_visitante)
        mutex_salida.release()
        plaza.remove(id_visitante)
        personas_dentro = len(plaza)
        visitantes_maximos.release()
    #si comprar_en es igual a 5, se va a The Cheesecake Factory
    if comprar_en == 5:
        print('Tengo ganas de romper la dieta, ¡iré a The Cheesecake Factory!\n')
        mutex_impresion.release()
        time.sleep(random.randint(5,11))
        mutex_salida.acquire()
        print('El visitante %d se va. ¡Vuleva pronto!\n' %id_visitante)
        mutex_salida.release()
        plaza.remove(id_visitante)
        personas_dentro = len(plaza)
        visitantes_maximos.release()
    #si comprar_en es igual a 6, se va a Cinemex
    if comprar_en == 6:
        print('Ya extrañaba ir al cine, ¡es hora de ir a Cinemex!\n')
        mutex_impresion.release()
        time.sleep(random.randint(5,11))
        mutex_salida.acquire()
        print('El visitante %d se va. ¡Vuleva pronto!\n' %id_visitante)
        mutex_salida.release()
        plaza.remove(id_visitante)
        personas_dentro = len(plaza)
        visitantes_maximos.release()
    
#Iniciamos las colas en las que se van a formar los visitantes para cada entrada
entrada_1 = []
entrada_2 = []
entrada_3 = []
entrada_4 = []
plaza=[]

#Establecemos mecanismos de sincronización
mutex_visitante = Semaphore(1)
mutex_salida = Semaphore(1)
mutex_impresion = Semaphore(1)

#Definimos el aforo máximo de la plaza
visitantes_maximos = Semaphore(20)

id_visitante=0
personas_dentro = 0
#cantidad total de vistantes del centro comercial
num_visitantes = 50
#cantidad total de entradas del centro comercial
num_entradas = 4
#invocamos a los hilos
for id_visitante in range(num_visitantes):
    Thread(target=visitantes, args=[id_visitante]).start()
for id_entrada in range(1,num_entradas+1):
    Thread(target=entradas, args=[id_entrada]).start()