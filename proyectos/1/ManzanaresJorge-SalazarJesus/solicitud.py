import time
import threading
import random

#Variables globales
estudiantes_reunidos = 0
error = 1
visitantes_formados = []


#Semáforos utilizados
mutex_estudiante = threading.Semaphore(1)
mutex_visitante = threading.Semaphore(1)
profesor_libre = threading.Semaphore(0)
jefe_esperando = threading.Semaphore(0)


#Definición del profesor
def Profesor():
    global severidad_profesor, num_estudiantes, num_jovenes, num_visitantes
    while(num_visitantes > 0):
        profesor_libre.acquire()
        print("P: La lista de visitantes formados es:", visitantes_formados)
        print("P: ¡Que entre el siguiente a verme!")
        time.sleep(random.random())
        num_visitantes = num_visitantes - 1
        mutex_visitante.acquire()
        if(visitantes_formados.pop(0) == -1):
            if(((num_jovenes*100/num_estudiantes) >= severidad_profesor) and ((num_jovenes*100/num_estudiantes) <= (100 - severidad_profesor))):
                print("P: ¡De acuerdo, les daré más tiempo de entrega!")
            else:
                print("P: ¡Sin excusas, la fecha de entrega no se mueve!")
        else:
            print("P: Visitante atendido")
        mutex_visitante.release()


#Definición del jefe de grupo
def JefeGrupo(id):
    jefe_esperando.acquire()
    print("J: Escribiendo los argumentos")
    time.sleep(2)
    print("J: Todos los argumentos escritos, toca ir a ver al profesor")
    mutex_visitante.acquire()
    visitantes_formados.append(id)
    print("J: Jefe de grupo formado para ver al profesor en la posición" )
    mutex_visitante.release()
    profesor_libre.release()


#Definición del estudiante
def Estudiante(id, tipo):
    global mutex_estudiante, estudiantes_reunidos, num_estudiantes
    time.sleep(random.random())
    mutex_estudiante.acquire()
    print("E: El estudiante %s número %d ha llegado a la reunión" %(tipo, id))
    estudiantes_reunidos = estudiantes_reunidos + 1
    if(estudiantes_reunidos == num_estudiantes):
        print("E: ¡Estamos todos reunidos!")
        jefe_esperando.release()
    mutex_estudiante.release()


#Definición del visitante
def Visitante(id):
    global mutex_visitante, visitantes_formados, profesor_libre
    time.sleep(5*random.random())
    mutex_visitante.acquire()
    visitantes_formados.append(id)
    print("V: Visitante %d está formado para ver al profesor" %id)
    mutex_visitante.release()
    profesor_libre.release()


