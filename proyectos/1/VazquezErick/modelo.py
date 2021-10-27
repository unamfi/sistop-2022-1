import threading
import random
import time

ORDENES = {
    1 : "PASTOR",
    2 : "SUADERO",
    3 : "CAMPECHANO",
}

NUM_ORDENES = len(ORDENES)

class Memoria(threading.Thread):

    """Clase que sirve para simular la memoria del taquero, la cual le avisara
    cuando haya algun pedido nuevo y cuando este saturado de pedidos olvidara alguno"""

    # variable para determinar cual es el limite de pedidos que un taquero puede recordar
    __LIMITE_DE_PEDIDOS_RECORDADOS = 5

    def __init__(self):
        super().__init__(target=self.saturacion_de_pedidos)
        self.pedidos = []

        # mutex para proteger la escritura  y lectura de los pedidos
        self.mutex_pedidos = threading.Semaphore(1)

        # semaforo para indicarle al taquero que se ponga a trabajar
        self.hay_pedido = threading.Semaphore(0)

    # metodo que guarda los pedidos nuevos
    def nuevo_pedido(self, pedido):
        self.mutex_pedidos.acquire()
        self.pedidos.append(pedido)
        self.mutex_pedidos.release()

        # una vez teniendo en memoria el pedido, el taquero se pone a trabajar
        self.hay_pedido.release()

    # metodo siempre activo que se encargara de olvidar los pedidos al sobresaturarse
    def saturacion_de_pedidos(self):
        while True:
            if len(self.pedidos) > self.__LIMITE_DE_PEDIDOS_RECORDADOS:
                
                # se escoge aleatoriamente un pedido para olvidar
                index = random.randint(0, len(self.pedidos) - 1)

                self.mutex_pedidos.acquire()
                pedido_olvidado = self.pedidos.pop(index)
                self.mutex_pedidos.release()


                print(" M : Olvidando pedido del cliente: %d" % pedido_olvidado.cliente.id)
                
                # al olvidar el pedido lo quitamos del trabajo que teniamos
                self.hay_pedido.acquire()
                
class Taquero(threading.Thread):
    
    """Esta clase sirve como representacion del taquero, el cual se encargara de atender
    los pedidos de los clientes"""

    def __init__(self, memoria: Memoria): 
        super().__init__(target=self.trabajando)
        self.memoria = memoria

    def trabajando(self):
        while True:

            # el taquero se duerme en la espera de chamba, su memoria le avisara cuando pase
            self.memoria.hay_pedido.acquire()

            self.memoria.mutex_pedidos.acquire()
            pedido_actual = self.memoria.pedidos.pop(0)
            self.memoria.mutex_pedidos.release()
            
            #print(pedido_actual.cliente.id, pedido_actual.orden)

            print("T: Trabajando en el pedido del Cliente %d" % pedido_actual.cliente.id)
            time.sleep(random.random())
            print("T: Terminando una orden de ", pedido_actual.orden ,"del Cliente %d" % pedido_actual.cliente.id)

            # le decimos al cliente que su pedido esta listo
            pedido_actual.cliente.esperando_pedido.release() 
                
        
class Cliente:

    """Clase cliente que encargara su orden al taquero"""

    def __init__(self, id, mi_taquero: Taquero):
        self.id = id
        self.mi_taquero = mi_taquero
        self.esperando_pedido = threading.Semaphore(0)
        self.enojometro = 0
        
        self.hilo_ordenar = threading.Thread(target=self.ordenar).start()
        self.hilo_espera = threading.Thread(target=self.espera)        
        
        self.do_run = True

    def solicitar_orden(self):
        orden = random.randint(1,NUM_ORDENES)
        self.mi_taquero.memoria.nuevo_pedido(Pedido(self, ORDENES[orden]))

    # cuando un cliente se crea inmediatamente toma una decision para
    # saber que va a pedir de comer al taquero entre las opciones de
    # las ordenes y espera en lo que su pedido esta lista. 
    def ordenar(self):
        #Se queda pensando en lo que decide que comer
        time.sleep(random.random())
        self.solicitar_orden()
        print("     C%d: Esperando pedido" % self.id)

        self.hilo_espera.start()
        self.esperando_pedido.acquire()

        if self.enojometro < 3:
            
            print("     C%d: Gracias :D" % self.id)
            self.do_run = False

    # cuando un cliente realiza su pedido comienza a esperar
    # por el, si no lo recibe en un tiempo x, su enojometro
    # comenzara a aumentar y podria ya no querer los tacos
    def espera(self):
        while getattr(self, "do_run", True):
            time.sleep(random.randint(1, 3))
            if self.enojometro == 3:
                print("     C%d: ya no quiero mis tacos, ya me voy" % self.id)
            self.enojometro += 1
        

class Pedido:
    
    """Clase sirve para representar las ordenes de los Clientes, la cual se vuelve
    en un pedido pues incluye ademas de la orden, quien fue quien la hizo para 
    poder identificarlo"""
    
    def __init__(self, cliente: Cliente, orden):
        self.cliente = cliente
        self.orden = orden

class Modelo(threading.Thread): 

    def __init__(self, controlador):
        super().__init__(target=self.arranque)
        self.controlador = controlador
        self.memoria = Memoria()
        self.taquero = Taquero(self.memoria)

    def arranque(self):
        # espera a que se inicie el programa en la interfaz
        self.controlador.esperando_inicio.acquire()
        self.taquero.start()
        self.memoria.start()

        for i in range(self.controlador.num_clientes):
            Cliente(i, self.taquero)