"""
Un profesor de la facultad asesora a varios estudiantes y estamos en su horario de atencion

Mision: modelar la interaccicon durante este horario de modo que la espera (para todos) sea 
lo mas corta posible

* Un profesor tiene x sillas en su cubiculo
    - Cuando no hay alumnos que atender, las sillas sirven como sofa, y el profesor se 
      acuesta a dormir la siesta

* Los alumnos pueden tocar a su puerta en cualquier momento, pero no pueden entrar mas de x 
  alumnos

* Para evitar coinfundir al profesor, solo un alumno puede presentar su duda (y esperar a su
  respuesta) al mismo tiempo. 

* Los demas alumnos sentados deben esperar pacientemente su turno 

* Cada alumno puede preguntar desde 1 y hasta 'y' preguntas (permitiendo que los demas alumnos
  pregunten entre una y otra)


DEFINICIONES PROPIAS: 

1. La probabilidad de llegada de un alumno es de 0.5
2. Pueden entrar al cubiculo una vez que se hayan juntado 3 alumnos 
3. se manejaran un maximo de 5 dudas por alumno por fines visualizacion en la ejecucion



"""

import threading
import time 
import random

alumnos_sentados = []

mutex = threading.Semaphore(1)
barrera = threading.Semaphore(0)
contador_alumnos = 0



def alumno(id): 
    global mutex, barrera, contador_alumnos
    
    #llego un alumno 
    if len(alumnos_sentados) < 5: #verifica si tiene espacio en el cubiculo
        mutex.acquire()
        print('\033[;37malumno sentadito: \033[;36m'+ str(id) )
        alumnos_sentados.append(id)
        contador_alumnos += 1
        mutex.release()
        barrera.release()

    else: #si no hay lugar se duerme y espera a que se desocupe
        print(f"\033[;37malumno \033[;36m{id} \033[;37mdice: no hay lugar mejor me duermo")
        time.sleep(random.random())
        pass

def profesor():
    global mutex, barrera, contador_alumnos

    while True:    
        print("\033[;33mESPERANDO A QUE SE JUNTEN ALUMNOS") 
        print(f"\033[;35mHAY {contador_alumnos} ALUMNOS EN ESPERA") #verifica si hay alumnos esperando ser atendidos
        
        if contador_alumnos >= 3: # pasa grupo de 3 alumnos
            print(f"\033[;32mPASANDO GRUPO DE {contador_alumnos} ALUMNOS")
            barrera.acquire()
            
            while alumnos_sentados: # mientras haya alumnos en su cubiculo
                a = alumnos_sentados.pop() # atendemos las dudas del primer alumno
                contador_alumnos -= 1 
                for duda in range(random.randint(1,5)):
                    print(f'\033[;37mATENDIENDO SU DUDA # \033[;31m{duda} \033[;37mALUMNO \033[;36m{a}')
                    time.sleep(random.random())
        else: 
            print('\033[;37mMIMIDO, NO MOLESTAR') #si no se ha juntado grupo de alumnos el profesor duerme
            time.sleep(5)

        
    
threading.Thread(target = profesor).start()

id = 0

while True: 
    threading.Thread(target=alumno,args=[id]).start()
    id += 1
    time.sleep(random.random())

    if id >= 10: 
        time.sleep(random.randint(10,15))

