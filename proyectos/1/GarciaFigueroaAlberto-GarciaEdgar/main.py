import threading 
import random
import time


#Recursos compartidos
contador_personas=0
mercancia=100

#Administración de procesos
estante_mutex= threading.Semaphore(1)
entrada_mutex= threading.Semaphore(1)
salida_mutex= threading.Semaphore(1)
caja_mutex= threading.Semaphore(1)
suministro=threading.Event()
ticket=threading.Event()
caja=threading.Event()

## La función empleado define el proceso que debe seguir para administrar los pagos
 
def Empleado(num):
    global id, caja
    runEmpleado(num)
    while(True):
        flag=caja.wait() #Esta bandera nos indica si un cliente a solicitado que se le cobren sus productos
        if flag:
            print(" ╬ El empleado despacha el pedido del cliente")
            ticket.set() #Una vez recibido el pago, se libera el ticket
            break
#Iniciamos hilo Empleado
def runEmpleado(numC):
    print(" ╬ Empleado "+str(numC)+" se prepara para trabajar")



##CLIENTE, define las acciones que debe realizar el cliente a lo largo del tiempo
def Cliente(num):
    global contador_personas
    runCliente(num)
    entrada_mutex.acquire() #Implementamos torniquete para evitar que entren más personas
    contador_personas+=1
    if contador_personas < 4:
        entrar(num)
    entrada_mutex.release()

#Inicia hilo cliente
def runCliente(numC):
    print(" ┼ Cliente "+str(numC)+" solicitando entrar") 

#Con el método agarrar, se define como el cliente adquiere sus productos, utilizando un mutex para evitar posibles problemas
def agarrar(num):
    global mercancia
    viendo=random.randint(1,6)
    time.sleep(viendo)
    print(" ┼ El cliente "+str(num)+" decide realizar una compra en la tienda")
    despensa=random.randint(5,100)
    estante_mutex.acquire()
    mercancia=mercancia-despensa
    if mercancia<20: #Cuando se detecte que el inventario se está acabando, avisamos al proveedor a traves de una bandera.
        print(" *** El inventario esta acabandose, el empleado debe llamar al provedor  *** ")
        suministro.set()
    estante_mutex.release()
    pagar(num)

#Método que inidica que un cliente ha solicitado el cobro de sus productos
def pagar(numC):
    global ticket
    caja_mutex.acquire()
    print(" ┼ El cliente "+str(numC)+" está pagando por sus articulos")
    caja.set()
    while True:
        flag=ticket.wait() #Avisamos al empleado que se ha iniciado el pago para que se generé su ticket
        if flag:
            caja_mutex.release()
            salir(numC)
            break

#Método que indica cuando un cliente está adentro de la tienda
def entrar(num):
    print(" ┼ El cliente "+str(num)+" entró a la tienda")
    agarrar(num)

#Método que indica que un cliente a salido de la tienda
def salir(num):
    global contador_personas
    print(" ┼ El cliente "+str(num)+ " ya compró y abandona la tienda")
    salida_mutex.acquire()
    contador_personas-=1
    salida_mutex.release()

##PROVEDOR, 
def Proveedor(num):
    runProveedor(num)
#Una vez que se detecta que se está acabando la mercancia, proveedor suministra más mercancia
def runProveedor(numC):
    global mercancia, suministro
    print(" = El proveedor "+str(numC)+" está listo para despachar, esperando la llamada de empleado") 
    suministro.wait(timeout=None)
    while True:
        if suministro.wait(timeout=None):
            estante_mutex.acquire()
            print(" = Estoy surtiendo los estantes con de la tienda")
            time.sleep(5)
            mercancia=100
            flag=suministro.clear()
            estante_mutex.release()    



# Almacenamos los hilos de actores
hilos_clientes = []  
hilos_empleados = []
hilos_proveedores= []
clientes_atendidos=0

def main():
    print("     ╔"+"═"*21+"╗")
    print("     ║ TIENDA DE DISFRACES ║")
    print("     ╚"+"═"*21+"╝")

    numClientes = int(input(" - ¿Cuántos clientes llegarán a la tienda?"))
    for k in range (1):
        hilos_proveedores.append(threading.Thread(target=Proveedor, args=[k])) #Creamos los hilos de los proovedores
        hilos_proveedores[k].start()
        time.sleep(1.5)
    for j in range (1):
        hilos_empleados.append(threading.Thread(target=Empleado, args=[j]))#Creamos los hilos de los empleados
        hilos_empleados[j].start()
        time.sleep(1.5)
    for i in range(numClientes):
        hilos_clientes.append(threading.Thread(target=Cliente, args=[i])) #Creamos los hilos de los clientes
        hilos_clientes[i].start()
        time.sleep(0.5)
    for k in range (1):     
        hilos_proveedores[k].join()
    for j in range (1):       
        hilos_empleados[j].join()
    for i in range(numClientes):
        hilos_clientes[i].join()

main()
