from threading import Semaphore,Thread, Barrier
import random
import time


def renos(num_reno):
    global c_renos
    while True:
        mut_renos_i.acquire()
        print('El reno %d se va de vacaciones' % num_reno)
        mut_renos_i.release()
        time.sleep(10)
        mut_renos_i.acquire()
        print('¡El reno %d ha vuelto!' % num_reno)
        mut_renos_i.release()
        mut_cuenta_renos.acquire()
        if c_renos == 0:
            barrera_renos.acquire()
        # Aumento la cuenta de los renos que volvieron
        c_renos = c_renos + 1
        # Si volvieron todos los renos
        if c_renos == total_renos:
            barrera_renos.release()
            c_renos = 0
            mut_renos_i.acquire()
            print('¡Despertamos a Santa porque ya estamos todos los renos!')
            print('Entregamos los regalos Jo, jo, jo')
            mut_renos_i.release()
        #Despertamos a santa
        santa_despierto.release()
            
        mut_cuenta_renos.release()
        barrera_renos.acquire()
        barrera_renos.release()
        
        
def santa():
    while True:
        # santa se duerme
        santa_despierto.acquire()
        print('Santa está dormido zzzz')
        time.sleep(10)
        
def elfos(num_elfo):
    while True:
        time.sleep(2)
        fallo = random.randint(1,100)
        
        #Asignamos el 3% de probabilidad
        if (fallo == 1 or fallo == 50 or fallo == 99):
            #El mutex lo usamos para que los hilos no se peleen por imprimir
            mut_elfos.acquire()
            print('Soy el elfo ',num_elfo,' y mi fallo es: ',fallo)
            mut_elfos.release()
            barrera_elfos.wait()

def impresion():
    #mut_elfos controla la impresion
    mut_elfos.acquire()
    print('¡Despertamos a Santa porque tenemos un problema!')
    mut_elfos.release()
    #Despertamos a santa
    santa_despierto.release()
    mut_elfos.acquire()
    print('He ayudado a todos los elfos ¡jo, jo, jo!')
    mut_elfos.release()
    
#Elementos renos
mut_renos_i = Semaphore(1) 
total_renos = 9
c_renos = 0
mut_cuenta_renos = Semaphore(1)
barrera_renos = Semaphore(1)

#Elementos Santa
santa_despierto = Semaphore(1)

#Elementos elfos
total_elfos = 200
barrera_elfos = Barrier(3,impresion)
mut_elfos = Semaphore(1)
mut_elfos_impresion = Semaphore(1)

#Programa principal
Thread(target=santa).start()

for num_elfo in range(total_elfos):
    Thread(target=elfos, args=[num_elfo]).start()

for num_reno in range(total_renos):
    Thread(target=renos, args=[num_reno]).start()
    
