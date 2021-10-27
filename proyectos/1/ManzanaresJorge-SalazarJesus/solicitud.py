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
    print("   El profesor se encuentra en su oficina listo para recibir visitas")
    print("")
    while(num_visitantes > 0):
        profesor_libre.acquire()
        print("   El profesor informa que la lista de visitantes formados es:", imprimeFila())
        print("   El profesor está llamando al siguiente visitante")
        time.sleep(random.random())
        num_visitantes = num_visitantes - 1
        mutex_visitante.acquire()
        if(visitantes_formados.pop(0) == -1):
            #Para que el profesor acepte la solicitud, debe haber un equilibrio entre ambos tipos de argumentos, sujeto a la severidad del profesor
            if(((num_jovenes*100/num_estudiantes) >= severidad_profesor) and ((num_jovenes*100/num_estudiantes) <= (100 - severidad_profesor))):
                print("   El profesor ha accedido a dar más tiempo para la entrega")
            else:
                print("   El profesor ha determinado que la fecha de entrega no se mueve")
        else:
            print("   El profesor ha terminado de atender al visitante")
        mutex_visitante.release()


#Definición del jefe de grupo
def JefeGrupo(id):
    print("   El jefe de grupo ha iniciado la reunión y está esperando a sus compañeros")
    print("")
    jefe_esperando.acquire()
    print("   El jefe de grupo está ecribiendo los argumentos")
    time.sleep(2)
    print("   El jefe de grupo ha escrito todos los argumentos y va a ir a ver al profesor")
    #Región crítica de visitante
    mutex_visitante.acquire()
    visitantes_formados.append(id)
    print("   El jefe de grupo está formado para ver al profesor en la posición" )
    mutex_visitante.release()
    profesor_libre.release()


#Definición del estudiante

def Estudiante(id, tipo):
    global mutex_estudiante, estudiantes_reunidos, num_estudiantes
    time.sleep(random.random())
    #Región crítica de estudiante
    mutex_estudiante.acquire()
    print(13*" "+"El estudiante %s número %d ha llegado a la reunión" %(tipo, id))
    estudiantes_reunidos = estudiantes_reunidos + 1
    if(estudiantes_reunidos == num_estudiantes):
            print(13*" "+"Los %d estudiantes están reunidos, es hora de deliberar" %(num_estudiantes))
            print("")
            jefe_esperando.release()
    mutex_estudiante.release()


#Definición del visitante
def Visitante(id):
    global mutex_visitante, visitantes_formados, profesor_libre
    time.sleep(5*random.random())
    #Región crítica de visitante
    mutex_visitante.acquire()
    visitantes_formados.append(id)
    print(13*" "+"El visitante %d está formado para ver al profesor" %id)
    mutex_visitante.release()
    profesor_libre.release()

#Método para imprimir la fila de visitantes formados
def imprimeFila():
    fila = ""
    for i in visitantes_formados:
        if(i==-1):
            fila += " jefe de grupo,"
        else:
            fila += " visitante " + str(i) + ","
    return fila[0:-1]

#Inicio del programa
print("")
print("")
print("                               BIENVENIDO")
print("")
while(error == 1):
    #Recopilación de datos a partir del usuario
    try:
        num_jovenes = int(input("          Ingrese el número de estudiantes jóvenes en el grupo: "))
        num_mayores = int(input("          Ingrese el número de estudiantes mayores en el grupo: "))
        num_visitantes = int(input("          Ingrese el número de visitantes extra para el profesor: ")) + 1
        severidad_profesor = int(input("          Ingrese que tan estricto es el profesor (0-50): "))
        print("")
        print("")
        num_estudiantes = num_jovenes + num_mayores
        error = 0
    except ValueError as e1:
        print("          Tipo de dato equivocado, ingrese los valores de nuevo, por favor")
        print("")


#Inicialización de los hilos
#Hilo del jefe de grupo
threading.Thread(target=JefeGrupo,args=[-1]).start()

#Hilo del profesor
threading.Thread(target=Profesor, args=[]).start()

print("")
#Hilos de estudiantes jóvenes
for k in range(num_jovenes):
    threading.Thread(target=Estudiante,args=[k, "joven"]).start()

#Hilos de estudiantes mayores
for i in range (num_mayores):
    threading.Thread(target=Estudiante,args=[num_jovenes + i, "mayor"]).start()

#Hilos de visitantes
for j in range (num_visitantes - 1):
    threading.Thread(target=Visitante,args=[j]).start()

