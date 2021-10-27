import threading 
import sys
import random
import time

#Declaramos los productos que se venden en la tienda
productos = {1:["disfraz de Dracula","Disfraz de zombie","disfraz de hombre lobo","disfraz de momia"], 2:["chocolate","caramelo","milkyway","pikafresas"]}

#Recursos compartidos
contador_personas=0
mercancia=100

#Administración de procesos
estante_mutex= threading.Semaphore()
entrada_mutex= threading.Semaphore()
suministro=threading.Event()
caja=threading.Event()

def runEmpleado(numC):
    print("Empleado "+str(numC)+" se prepara para trabajar")

def runCliente(numC):
    print("Cliente "+str(numC)+" solicitando entrar") 

def runProveedor(numC):
    global mercancia, suministro
    print("Proveedor "+str(numC)+" listo para despachar, esperando llamada...")
    while(True):
        estante_mutex.acquire()
        if suministro:
            print("Surtiendo estantes....")
            time.sleep(5)
            mercancia=100
            estante_mutex.release()
            suministro=False
    

def cobrar(numC,numE):
    print("Empleado "+str(numE)+" cobra los articulos de cliente"+str(numC))

def pagar(numC,numE):
    caja.set()
    print("Cliente "+str(numE)+" paga los articulos"+str(numC))

def solicitarMercancia(numE):
    print("Llamando al prooveedor")

def entregarMercancia():
    print("El proveedor despacha mercancia")

def entrar(num):
    print("El cliente "+str(num)+" entró a la tienda")
    agarrar()


def agarrar():
    global mercancia,suministro
    print("El cliente se decide a comprar algun objeto :0")
    viendo=random.randint(1,6)
    despensa=random.randint(5,100)
    time.sleep(viendo)
    estante_mutex.acquire()
    mercancia=mercancia-despensa
    print(mercancia)
    if mercancia<20:
        print("----------"+str(mercancia))
        suministro.set()
    estante_mutex.release()
    pagar()

def Cliente(num):
    global contador_personas
    runCliente(num)
    entrada_mutex.acquire()
    contador_personas+=1
    entrada_mutex.release()
    if contador_personas < 8:
        entrar(num)

def Empleado(num):
    global id, caja
    runEmpleado(num)
    while(True):
        caja.

def Proveedor(num):
    runProveedor(num)

def Tienda():
    print("")

# Almacenamos los hilos de los elfos y renos
hilos_clientes = []  
hilos_empleados = []
hilos_proveedores= []
def main():
    
    for k in range (1):
        hilos_proveedores.append(threading.Thread(target=Proveedor, args=[k])) #Creamos los hilos de los proovedores
        hilos_proveedores[k].start()
        time.sleep(1.5)
    for j in range (1):
        hilos_empleados.append(threading.Thread(target=Empleado, args=[j]))
        hilos_empleados[j].start()
        time.sleep(1.5)
    for i in range(10):
        hilos_clientes.append(threading.Thread(target=Cliente, args=[i]))
        hilos_clientes[i].start()
        time.sleep(0.5)
main()
