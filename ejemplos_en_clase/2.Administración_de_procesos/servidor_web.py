#!/usr/bin/python3
#
# Reglas:
# - Al inicializar, el proceso jefe lanza 'k' hilos trabajadores
#   - Los trabajadores que no tienen nada que hacer se van a dormir
# - El proceso jefe recibe una conexión de red, y elige a cualquiera de los trabajadores para que la atienda
#   - Se le asigna a un trabajador, y lo despierta
# - El jefe va a buscar mantener siempre a 'k' hilos disponibles y listos para atender las solicitudes que van llegando
#
# Refinamiento:
# - Cada hilo debe notificar antes de terminar su ejecución, entregando información de rendimiento
import threading
import time
import random

k = 10  # Hilos trabajadores en espera
despiertaTrabajador = threading.Semaphore(0)
solicitudCliente = threading.Semaphore(0)
trabajadores = 0
mut_trabajadores = threading.Semaphore(1)
mut_contabilidad = threading.Semaphore(1)
contabilidad = []

def jefe():
    global k, solicitudCliente
    # En la inicialización: Lanzamos 'k' hilos trabajadores
    print('J: Inicializando. Lanzo %d hilos trabajador' % k)
    for i in range(k):
        threading.Thread(target=trabajador, args=[]).start()
    # Me mantengo siempre trabajando en el siguiente ciclo:
    # Cada vez que llega una solicitud del cliente, libero un
    # hilo para que la atienda
    while True:
        print('J: Esperando solicitud')
        solicitudCliente.acquire()
        print('J: Despertando trabajador')
        despiertaTrabajador.release()
        print('J: Creando nuevo trabajador')
        threading.Thread(target=trabajador, args=[]).start()

def trabajador():
    global despiertaTrabajador, trabajadores, mut_trabajadores
    mut_trabajadores.acquire()
    trabajadores += 1
    yo_soy = trabajadores

    mut_trabajadores.release()
    print('   T%02d: Inicializado. ¡A dormir en lo que llega chamba!' % yo_soy)

    despiertaTrabajador.acquire()
    print('   T%02d: Atendiendo solicitud...' % yo_soy)
    tiempo_atencion = random.random()
    time.sleep(tiempo_atencion)

    mut_contabilidad.acquire()
    contabilidad.append([yo_soy, tiempo_atencion])
    mut_contabilidad.release()
    # ¡Me voy a casita!
    print('   T%02d: Terminé. ¡A descansar!' % yo_soy)

def contador():
    while True:
        time.sleep(10)

        mut_contabilidad.acquire()
        # Reporta el contenido de contabilidad
        longitud = len(contabilidad)
        promedio = 0
        mínimo = [None, 1]
        máximo = [None, 0]
        for i in range(longitud):
            promedio += contabilidad[i][1]
            if contabilidad[i][1] < mínimo[1]:
                mínimo = [contabilidad[i][0], contabilidad[i][1]]
            if contabilidad[i][1] > máximo[1]:
                máximo = [contabilidad[i][0], contabilidad[i][1]]
        promedio = promedio / longitud
        mut_contabilidad.release()

        print('        HORA DEL RESUMEN CONTABLE')
        print('        =========================')
        print('        Hemos atendido %d solicitudes' % longitud)
        print('        El tiempo promedio de atención es de %1.3f segundos' % promedio)
        print('        El trabajador más rápido fue %d, con %1.3f segundos' % (mínimo[0], mínimo[1]))
        print('        El trabajador más lento fue %d, con %1.3f segundos' % (máximo[0], máximo[1]))

def lanza_clientes():
    global solicitudCliente
    while True:
        time.sleep(random.random() / 3.0)
        print('      C: ¡Nueva solicitud!')
        solicitudCliente.release()

threading.Thread(target=jefe, args=[]).start()
threading.Thread(target=contador, args=[]).start()
lanza_clientes()
