import threading, queue
import time

# El problema es parecido al productor-consumidor,
# sin embargo, en este caso una vez que se atienda a un
# alumno, se enviará a la cola de nuevo en caso de que
# aún tenga preguntas disponibles (tiene y inicialmente)
buf = queue.Queue()

# Máximo número de alumnos en el salón de clase
x = 10
# Máximo número de preguntas por alumno
y = 5

# Id de los alumnos
eid = 1
eid_lock = threading.Lock()

# Mutex de la cola de estudiantes
mutex = threading.Semaphore(1)
# Semáforo con el total de alumnos en la cola
estudiantes = threading.Semaphore(0)


class Estudiante:
    def __init__(self, eid):
        self.preguntas_restantes = y
        self.id = eid
    
    def preguntas_se_acabaron(self):
        return self.preguntas_restantes == 0
    
    def hacer_pregunta(self):
        print("Estudiante " + str(self.id) + " hizo una pregunta")
        time.sleep(0.5)
        # Actualizar el número de preguntas de este estudiante
        self.preguntas_restantes -= 1

# Llenar el salón de clases
def llenar_salon_inicial():
    for i in range(x):
        producir_estudiante()

# Simular que los alumnos llegan después de haber iniciado
def llenar_salon_periodicamente():
    while True:
        producir_estudiante()
        time.sleep(5)

# Añadir un estudiante al salón de clases para que sea
# atendido. De no haber lugar, será rechazado
def producir_estudiante():
    global eid
    # Generar estudiante con nuevo id
    with eid_lock:
        estudiante = Estudiante(eid)
        eid = eid + 1
    
    mutex.acquire()
    # Hay espacio en el salón, agregar estudiante
    if buf.qsize() < x:
        buf.put(estudiante)
        print("Estudiante agregado (" + str(estudiante.id) + ")")
        estudiantes.release()
    # No hay espacio, rechazarlo
    else:
        print("Estudiante " + str(estudiante.id) + " rechazado")
    mutex.release()

# El profesor atenderá a los estudiantes presentes en el
# salón de clase. Estos estarán formados en una cola. Cuando
# un estudiante es atendido, se envía al final de la "fila"
# para atender a los demás estudiantes lo más rápido posible.
# Cuando un estudiante termina todas sus preguntas, sale del
# salón (se elimina de la cola), dejando un espacio libre para
# otro estudiante.
def profe_consumidor():
    while True:
        mutex.acquire()

        estudiante = buf.get()
        estudiante.hacer_pregunta()
        # Sacarlo del salón
        if estudiante.preguntas_se_acabaron():
            print("Estudiante " + str(estudiante.id) + " terminó sus preguntas")
            estudiantes.acquire()
        # Enviarlo al final de la fila
        else:
            buf.put(estudiante)
        
        mutex.release()
        time.sleep(1.5)


llenar_salon_inicial()
# El productor estará enviando estudiantes al salón
threading.Thread(target=llenar_salon_periodicamente, args=[]).start()
profe_consumidor()
