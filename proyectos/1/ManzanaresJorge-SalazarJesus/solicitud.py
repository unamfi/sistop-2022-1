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


#Inicio del programa
while(error == 1):
    #Recopilación de datos a partir del usuario
    try:
        num_jovenes = int(input('Ingrese el número de estudiantes jóvenes en el grupo: '))
        num_mayores = int(input('Ingrese el número de estudiantes mayores en el grupo: '))
        num_visitantes = int(input('Ingrese el número de visitantes extra para el profesor: ')) + 1
        severidad_profesor = int(input('Ingrese que tan estricto es el profesor (0-50): '))
        num_estudiantes = num_jovenes + num_mayores
        error = 0
    except ValueError as e1:
        print("Tipo de dato equivocado")


#Inicialización de los hilos
#Hilo del jefe de grupo
threading.Thread(target=JefeGrupo,args=[-1]).start()

#Hilo del profesor
threading.Thread(target=Profesor, args=[]).start()

#Hilos de estudiantes jóvenes
for k in range(num_jovenes):
    threading.Thread(target=Estudiante,args=[k, "joven"]).start()

#Hilos de estudiantes mayores
for i in range (num_mayores):
    threading.Thread(target=Estudiante,args=[num_jovenes + i, "mayor"]).start()

#Hilos de visitantes
for j in range (num_visitantes - 1):
    threading.Thread(target=Visitante,args=[j]).start()
