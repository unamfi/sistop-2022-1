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
estante_mutex= threading.Semaphore(1)
entrada_mutex= threading.Semaphore(1)
salida_mutex= threading.Semaphore(1)
caja_mutex= threading.Semaphore(1)
suministro=threading.Event()
caja=threading.Event()
ticket=threading.Event()

def runEmpleado(numC):
    print(" ╬ Empleado "+str(numC)+" se prepara para trabajar")

def runCliente(numC):
    print(" ┼ Cliente "+str(numC)+" solicitando entrar") 

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
            
    

#def cobrar(numC,numE):
#    print("Empleado "+str(numE)+" cobra los articulos de cliente"+str(numC))

def pagar(numC):
    global ticket
    caja_mutex.acquire()
    print(" ┼ El cliente "+str(numC)+" está pagando por sus articulos")
    caja.set()
    while True:
        flag=ticket.wait()
        if flag:
            caja_mutex.release()
            salir(numC)
            break

# def solicitarMercancia(numE):
#     print(" ╬ El empleado llama al prooveedor por más producto")

# def entregarMercancia():
#     print("El proveedor despacha mercancia")

def salir(num):
    global contador_personas
    print(" ┼ El cliente "+str(num)+ " ya compró y abandona la tienda")
    salida_mutex.acquire()
    contador_personas-=1
    salida_mutex.release()

def entrar(num):
    print(" ┼ El cliente "+str(num)+" entró a la tienda")
    agarrar(num)


def agarrar(num):
    global mercancia
    viendo=random.randint(1,6)
    time.sleep(viendo)
    print(" ┼ El cliente "+str(num)+" decide realizar una compra en la tienda")
    despensa=random.randint(5,100)

    estante_mutex.acquire()
    mercancia=mercancia-despensa
    if mercancia<20:
        print(" *** El inventario esta acabandose, el empleado debe llamar al provedor  *** ")
        suministro.set()
    estante_mutex.release()
    pagar(num)

def Cliente(num):
    global contador_personas
    runCliente(num)
    entrada_mutex.acquire()
    contador_personas+=1
    if contador_personas < 4:
        entrar(num)
    entrada_mutex.release()
   

def Empleado(num):
    global id, caja
    runEmpleado(num)
    while(True):
        flag=caja.wait()
        if flag:
            print(" ╬ El empleado despacha el pedido del cliente")
            ticket.set()
            break

def Proveedor(num):
    runProveedor(num)


# Almacenamos los hilos de actores
hilos_clientes = []  
hilos_empleados = []
hilos_proveedores= []
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
        hilos_empleados.append(threading.Thread(target=Empleado, args=[j]))
        hilos_empleados[j].start()
        time.sleep(1.5)
    for i in range(numClientes):
        hilos_clientes.append(threading.Thread(target=Cliente, args=[i]))
        hilos_clientes[i].start()
        time.sleep(0.5)
main()
